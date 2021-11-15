from django.contrib import admin
from .models import CustomUser, Message, Fcm


admin.site.register(CustomUser)
admin.site.register(Message)
admin.site.register(Fcm)
