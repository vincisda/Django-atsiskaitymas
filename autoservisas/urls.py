"""autoservisas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Autoservice.views import home_view, login_view, register_view, statistics_view, order_view, car_create_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('statistics/', statistics_view, name='statistics_view'),
    path('order/', order_view, name='order_view'),
    path('car/', car_create_view, name='car_create_view'),
    path('admin/', admin.site.urls),
    
    
]
