from django.http import HttpResponse
from django.shortcuts import render

from .models import Car,CarModel, Service, OrderRow, Order

# Create your views here.

def home_view(request ,*args, **kwargs):

    return render(request, 'home.html', {})


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        pass

    return render(request, 'login.html', {})


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        pass

    return render(request, 'register.html', {})


def statistics_view(request, *args, **kwargs):
    all_cars= Car.objects.all()
    return render(request, 'stats.html',
     {'all_cars': all_cars,
     
     })


def order_view(request, *args, **kwargs):

    return render(request, 'order.html', {})


def car_view(request, *args, **kwargs):

    return render(request, 'auto.html', {})