# В файле routing.py вашего приложения

from django.urls import path
from .views import UserChatWebsocket

websocket_urlpatterns = [
    path('ws/chats/<int:chat_id>', UserChatWebsocket.as_asgi()),
]
