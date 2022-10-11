from django.db.models.signals import post_save, pre_save

from .models import NamecardDesign, NamecardPool, Visitor

import urllib, json, os


def post_message(url, data):
    headers = {
        'Content-Type': 'application/json',
    }
    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()


def CreateVisitorSignal(sender, instance, created, **kwargs):
    if created:
        context = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"> *ニックネーム*\n> {instance.nickname}\n>*メールアドレス*\n> {instance.email}\n>*No.*\n> {instance.pk}"
                    }
                }
            ]
        }
        if os.environ.get('SLACK_URL'):
            post_message(os.environ.get('SLACK_URL'), context)

post_save.connect(CreateVisitorSignal, Visitor)


def UpdateRegistrationNamecardSignal(sender, instance, **kwargs):
    namecarddesign = NamecardDesign.objects.filter(pk=instance.pk).first()
    if namecarddesign:
        amount = namecarddesign.numofprints - instance.numofprints
        if amount > 0:
            NamecardPool.objects.bulk_create([NamecardPool(namecard=namecarddesign) for _ in range(amount)])
        elif amount < 0:
            instance.numofprints = namecarddesign.numofprints

pre_save.connect(UpdateRegistrationNamecardSignal, NamecardDesign)


def CreateRegistrationNamecardSignal(sender, instance, created, **kwargs):
    if created:
        namecarddesign = NamecardDesign.objects.get(pk=instance.pk)
        NamecardPool.objects.bulk_create([NamecardPool(namecard=namecarddesign) for _ in range(instance.numofprints)])

post_save.connect(CreateRegistrationNamecardSignal, NamecardDesign)