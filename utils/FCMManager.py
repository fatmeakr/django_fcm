import firebase_admin
import os
from firebase_admin import credentials, messaging

data = os.path.abspath(os.path.dirname(__file__)) + "/fcm-project-certification.json"
cred = credentials.Certificate(data)
firebase_admin.initialize_app(cred)


def sendPush(title, msg, registration_token, dataObject=None):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(title=title,
                                            body=msg,
                                            ),
        data=dataObject,
        tokens=[registration_token]
    )

    response = messaging.send_multicast(message)
    print('successfully sent message', response)
