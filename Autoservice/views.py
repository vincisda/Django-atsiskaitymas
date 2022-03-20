from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request ,*args, **kwargs):

    return render(request, 'home.html', {})


def login_view(request, *args, **kwargs):

    return render(request, 'login.html', {})


def register_view(request, *args, **kwargs):

    return render(request, 'register.html', {})


def statistics_view(request, *args, **kwargs):

    return render(request, 'stats.html', {})