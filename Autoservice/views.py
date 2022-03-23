from django.http import HttpResponse
from django.shortcuts import render

from .models import Car, CarModel, Service, OrderRow, Order
from .forms import  RawCarForm
# Create your views here.

######################***PAGE VIEWS***###############################################
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
    all_models = CarModel.objects.all()
    return render(request, 'stats.html',
     {'all_cars': all_cars,
     'all_models': all_models,
     
     })


def order_view(request, *args, **kwargs):

    return render(request, 'order.html', {})


####################***FORM VIEWS***######################################


def car_create_view(request):
    my_form = RawCarForm()
    print(request.method)
    if request.method == 'POST':
        my_form = RawCarForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
        else:
            print(my_form.errors)

    context = {'my_form': my_form}
    return render(request, 'auto.html', context)