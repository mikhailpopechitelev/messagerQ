from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    #path('', cache_page(60*5)(ChatsHome.as_view()), name = 'chats'),
    path('', ChatsHome.as_view(), name = 'chats'),
    path('<int:chat_id>/', UserChat.as_view() , name = 'chat'),
    path('logout', logout_user, name="logout"),
    path('registration', RegisterUser.as_view(), name = 'registration'), 
    path('login', LoginUser.as_view(), name="login"),

]


handler404 = pageNotFound