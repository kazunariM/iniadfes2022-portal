from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from ... import models
from ..serializers import reception as serializers


class ConfirmVisitorAPI(RetrieveAPIView):
    serializer_class = serializers.ConfirmVisitorSerializer
    lookup_field = 'management_uuid'
    queryset = models.Visitor


class SelectNamecardAPI(APIView):
    serializer_class = serializers.SelectNamecardSerializer

    def post(self, request):
        visitor = models.Visitor.objects.filter(management_uuid=request.data["management_uuid"]).first()
        namecardpool = models.NamecardPool.objects.filter(qrid=request.data["userid"], used=False).first()
        if visitor and namecardpool:
            visitor.userid = namecardpool.qrid
            visitor.identifying = namecardpool.pk
            visitor.save()

            namecardpool.used = True
            namecardpool.save()
            
            return Response({"nickname" : visitor.nickname, "identifying" : visitor.identifying})
        
        return Response({}, status=400)


class HandedoverAPI(UpdateAPIView):
    serializer_class = serializers.HandedoverSerializer
    lookup_field = 'management_uuid'
    queryset = models.Visitor
