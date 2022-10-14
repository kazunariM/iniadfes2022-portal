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
        amount = instance.numofprints - namecarddesign.numofprints
        if amount > 0:
            NamecardPool.objects.bulk_create([NamecardPool(namecard=namecarddesign) for _ in range(amount)])
            instance.numofremaining += amount
        elif amount < 0:
            namecardpool = NamecardPool.objects.filter(namecard=namecarddesign, used=False)
            amount = len(namecardpool) if len(namecardpool) < abs(amount) else -amount
            [item.delete() for item in namecardpool[0:amount]]
            instance.numofremaining -= amount
    else:
        instance.numofremaining = instance.numofprints
            
pre_save.connect(UpdateRegistrationNamecardSignal, NamecardDesign)


def CreateRegistrationNamecardSignal(sender, instance, created, **kwargs):
    if created:
        namecarddesign = NamecardDesign.objects.get(pk=instance.pk)
        NamecardPool.objects.bulk_create([NamecardPool(namecard=namecarddesign) for _ in range(instance.numofprints)])

post_save.connect(CreateRegistrationNamecardSignal, NamecardDesign)


def CreateVisitorSignal(sender, instance, created, **kwargs):
    if created:
        instance.design.numofremaining = instance.design.numofprints - len(instance.design.visitors_select.all())
        instance.design.save()
        
post_save.connect(CreateVisitorSignal, Visitor)
