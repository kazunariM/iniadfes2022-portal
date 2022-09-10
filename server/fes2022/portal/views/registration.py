from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404

from ..serializers import registration as serializer
from ... import models
from ... import event_schedule

import datetime, os, qrcode, io

# Create your views here.


class RegistrationView(CreateAPIView):
    serializer_class = serializer.RegistrationSerializer

    def perform_create(self, serializer):
        context = {
            'protocol': self.request.scheme,
            'domain' : get_current_site(self.request).domain,
            'visitor' : serializer.save(),
        }
        subject = render_to_string('mails/registration_subject.txt', context)
        message = render_to_string('mails/registration_text.txt', context)

        email = EmailMessage(subject, message, os.environ.get('EMAIL_HOST_USER'), [context["visitor"].email], [os.environ.get('EMAIL_HOST_USER')])
        email.send()


class NamecardView(ListAPIView):
    serializer_class = serializer.NamecardSerializer

    def get_queryset(self):
        return \
            models.NamecardDesign.objects.all() \
            if datetime.date.today() < event_schedule.PREREGISTRATION \
            else models.NamecardDesign.objects.filter(is_only_advance=False)


class CompleteView(RetrieveAPIView):
    queryset = models.Visitor
    serializer_class = serializer.CompleteSerializer
    lookup_field = 'management_uuid'

    def get_object(self):
        visitor = get_object_or_404(self.queryset, management_uuid=self.kwargs[self.lookup_field])
        if not visitor.is_verified_email:
            visitor.is_verified_email = True
            visitor.save()

            qr = qrcode.make(visitor.management_uuid)
            img_bytes = io.BytesIO()
            qr.save(img_bytes, format='PNG')

            context = {
                'visitor' : visitor,
            }

            subject = render_to_string('mails/send_management_QR_subject.txt', context)
            message = render_to_string('mails/send_management_QR_text.txt', context)

            email = EmailMessage(subject, message, os.environ.get('EMAIL_HOST_USER'), [visitor.email])
            email.attach('受付用QRコード.png', img_bytes.getvalue())
            email.send()

        return visitor
    