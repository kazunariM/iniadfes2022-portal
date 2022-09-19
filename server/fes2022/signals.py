from django.db.models.signals import post_save

from .models import Visitor

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
                        "text": f"> *氏名*\n> {instance.last_name} {instance.first_name}さん\n> *ニックネーム*\n> {instance.nickname}\n>*メールアドレス*\n> {instance.email}\n>*整理番号*\n> {instance.pk}"
                    }
                }
            ]
        }
        if os.environ.get('SLACK_URL'):
            post_message(os.environ.get('SLACK_URL'), context)

post_save.connect(CreateVisitorSignal, Visitor)