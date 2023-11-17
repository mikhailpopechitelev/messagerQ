from django.shortcuts import render
from django.http import HttpResponse
from .models import * 

# Create your views here.
def index(request):
    return render(request, 'chats/index.html')

def newsfeed(request):
    return render(request, 'chats/newsfeed.html')

def indexchats(request, chatid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{chatid}</p>")

def pageNotFound(request, exception):
    return HttpResponse('<h1>Cтраница не найдена</h1>')