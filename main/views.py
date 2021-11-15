from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import SendMessageSerializer, FcmSerializer
from .models import Message, Fcm


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = SendMessageSerializer
    permission_classes = [AllowAny]


class FcmGeneratorView(generics.CreateAPIView):
    queryset = Fcm.objects.all()
    serializer_class = FcmSerializer
    permission_classes = [AllowAny]
