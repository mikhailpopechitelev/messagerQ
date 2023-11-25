from typing import Any, Dict
from django.contrib.auth import logout
from django.db.models.query import QuerySet
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from .forms import *
from .utils import *
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.core.cache import cache



class ChatsHome(DataMixin, ListView):
    model = User
    template_name = 'chats/index.html'
    context_object_name = 'friends'
    extra_context = {'title':'Главная страница чатов'}

    def get_queryset(self):
        friends = cache.get('friends')
        if not friends:
            result = Friendships.objects.filter(firstusr__pk= self.request.user.id).values_list('secondusr', flat=True)
            third_elements = [item for item in result]
            friends = User.objects.filter(pk__in = third_elements)
            cache.set('friends',friends, 60*2)
        return friends
    
    #когда подгружать инфу нужно динамически
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs) 
        if 'chat_selected' not in context:
            context['chat_selected'] = 0
            context['user_id'] = self.request.user.id
        return context
    
    #когда подгружать инфу нужно динамически
    #def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #    context = super().get_context_data(**kwargs) 
    #    c_def = self.get_user_context()
    #    context = dict(list(context.items())+ list(c_def.items('title''Главная страница чатов')))
    #    return context
    
    
#def index(request):
#    friends = User.objects.all()
#    return render(request, 'chats/index.html',{'friends': friends,'title':'Главная страница чатов'})

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

class UserChat(ListView):
    model = Messages
    template_name = 'chats/index.html'
    context_object_name = 'messages'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
    #все сообщения принадлежащие такущему id чату
    #def get_queryset(self):
    #    return Messages.objects.filter(cat__slug=self.kwargs['cat_slug', is_published = True])

def pageNotFound(request, exception):
    return HttpResponse('<h1>Cтраница не найдена</h1>')

def logout_user(request):
    logout(request)
    return redirect('login')