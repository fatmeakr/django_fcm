from rest_framework import serializers
from utils.MakeMessage import send_push_notification
from .models import Message, Fcm


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['title', 'body']

    def create(self, validated_data):
        current_user = self.context['request'].user
        instance = Message.objects.create(user_id=current_user.id, **validated_data)
        send_push_notification('Welcome', 'Your registration done successfuly.', current_user )
        return instance


class FcmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fcm
        fields = ('id', 'token', 'user')
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        current_user = self.context['request'].user
        instance, created = Fcm.objects.update_or_create(user_id=current_user.id, defaults=validated_data)
        return instance
