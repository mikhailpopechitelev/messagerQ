from typing import Any, Dict
from django.contrib.auth import logout
from django.db.models.query import QuerySet
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import * 
from .forms import *
from .utils import *
from django.views.generic import ListView, CreateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.core.cache import cache
from django.contrib.auth.models import User
from django.http import JsonResponse

def get_latest_messages(request, chat_id):
    messages = Messages.objects.filter(chat=chat_id).order_by('-created_at')[:20]
    message_data = [{'time': msg.created_at.strftime('%H:%M'), 'text': msg.text, 'sender': msg.sender.username} for msg in messages]
    return JsonResponse({'messages': message_data})

class ChatsHome(DataMixin, ListView):
    model = User
    template_name = 'chats/index.html'
    context_object_name = 'chats'
    extra_context = {'title':'Главная страница чатов'}

    def get_queryset(self):
        user_chats = Chatparticipant.objects.filter(participant=self.request.user.id).values_list('chat', flat=True)
        chats = Chats.objects.filter(id__in=user_chats)
        #print(chats)
        #result = Friendships.objects.filter(firstusr__pk= self.request.user.id).values_list('secondusr', flat=True)
        #third_elements = [item for item in result]
        #friends = User.objects.filter(pk__in = third_elements)
        #friends = cache.get('friends')
        #if not friends:
        #    result = Friendships.objects.filter(firstusr__pk= 1).values_list('secondusr', flat=True)
        #    print(result)
        #    third_elements = [item for item in result]
        #    print(third_elements)
        #    friends = User.objects.filter(pk__in = third_elements)
        #    cache.set('friends',friends, 60*2)
        return chats
    
    #когда подгружать инфу нужно динамически
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs) 
        if 'chat_selected' not in context:
            context['chat_selected'] = 0
            context['user_id'] = self.request.user.id
        return context
    
    
class UserChat(DataMixin, ListView):
    model = Chats
    template_name = 'chats/chat.html'
    context_object_name = 'messages'
    paginate_by = 10
    
    
    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        messages = Messages.objects.filter(chat=chat_id).order_by('-created_at')[:20]
        return messages
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['chat_id'] = self.kwargs['chat_id']
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

def newsfeed(request):
    return render(request, 'chats/newsfeed.html')


class LoginUser(LoginView):
    #form_class = UserCreationForm
    form_class = AuthenticationForm
    template_name = 'chats/login.html'
    
    def get_success_url(self):
        return reverse_lazy('chats')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'chats/registration.html'
    success_url = reverse_lazy('login')
    
#def authorization(request):
#    if request.method == 'POST':
#        form = AuthorizationForm(request.POST)
#        if form.is_valid():
#           try:
#                form.save()
#                return redirect('chats')
#            except:
#                form.add_error(None, 'Ошибка авторизации пользователя')
#    else:
#        form = AuthorizationForm()
#    return render(request, 'chats/authorization.html')


def pageNotFound(request, exception):
    return HttpResponse('<h1>Cтраница не найдена</h1>')

def logout_user(request):
    logout(request)
    return redirect('login')