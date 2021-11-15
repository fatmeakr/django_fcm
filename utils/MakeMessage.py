
from django.core.exceptions import ObjectDoesNotExist
from utils.FCMManager import sendPush
from main.models import Fcm


def send_push_notification(title, body, user):
    try:
        fcm_token = Fcm.objects.get(user=user)
        try:
            sendPush(str(title), str(body), fcm_token.token)
        except ObjectDoesNotExist:
            pass
    except ObjectDoesNotExist:
        pass
