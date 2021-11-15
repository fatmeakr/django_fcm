from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    password = models.CharField(max_length=128, null=True, blank=True)
    mobile_number = models.CharField(max_length=30, blank=True, null=True, unique=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'mobile_number'

    def __str__(self):
        return f"{self.mobile_number}"

    def __repr__(self):
        return self.__str__()


class Message(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField()
    user = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}: {self.title}"


class Fcm(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT, related_name='user_fcm_token')
    token = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"
