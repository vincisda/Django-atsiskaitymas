from ast import Or
from django.contrib import admin

# Register your models here.
from .models import Car, Order, CarModel, Service, OrderRow

admin.site.register(Car)
admin.site.register(Order)
admin.site.register(CarModel)
admin.site.register(Service)
admin.site.register(OrderRow)