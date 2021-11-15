from django.urls import path
from . import views


urlpatterns = [
    path('message/', views.MessageCreateView.as_view(), name='message_create'),
    path('fcm/', views.FcmGeneratorView.as_view(), name='fcm_create'),
]
