from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'chats'),
    path('<int>:chatid/', indexchats, name = 'chat'),
    path('newsfeed/', newsfeed, name ='newsfeed'),
]

handler404 = pageNotFound