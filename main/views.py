from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict = {
        'title': 'Home',
        'content': 'Главная страница магазина'

    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')