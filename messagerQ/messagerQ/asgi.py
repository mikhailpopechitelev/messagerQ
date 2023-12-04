"""
ASGI config for messagerQ project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messagerQ.settings')

application = get_asgi_application()

"""
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter
# from channels.routing import URLRouter

# from django.core.asgi import get_asgi_application
# from django.urls import path


# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourproject.settings')


# from chats.consumers import YourConsumer


# django_asgi_app = get_asgi_application()

# application = ProtocolTypeRouter({
#     'http': django_asgi_app,
#     'websocket': AuthMiddlewareStack(
#         URLRouter([
#             path('ws', YourConsumer.as_asgi())
#         ])
#     )
# })

from channels.routing import ProtocolTypeRouter, URLRouter
from chats.routing import websocket_urlpatterns  # Импортируйте ваши URL из файла routing.py
import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack

#os.environ['DJANGO_SETTINGS_MODULE'] = 'messagerQ.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messagerQ.settings')
#application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        ),
    }
)