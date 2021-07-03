from django.shortcuts import render
from mainapp.models import Colors
import random


def index(request):
    colors = Colors.objects.all()
    context = {
        'page_title': 'Главная',
        'color': random.choice(colors),
    }
    return render(request, 'mainapp/index.html', context)


def about_us(request):
    context = {
        'page_title': 'О нас',
    }
    return render(request, 'mainapp/about_us.html', context)


def login(request):
    context = {
        'page_title': 'Авторизация',
    }
    return render(request, 'mainapp/login.html', context)
