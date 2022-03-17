from django.db import models

# Create your models here.



class CarModel(models.Model):
    make  = models.CharField(max_length=100)
    model = models.CharField(max_length=100) 


class Car(models.Model):
    state_registration = models.CharField(max_length=20, null=False )
    car_model_id       = models.ForeignKey(CarModel, on_delete=models.CASCADE) 
    vin_code           = models.CharField(max_length=30)
    client             = models.CharField(max_length=100)


class Order(models.Model):
    date   = models.DateField()
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)


class Service(models.Model):
    name  = models.CharField(max_length=20, null=False )
    price = models.DecimalField(max_digits=20, decimal_places=2)


class OrderRow(models.Model):
    order_id   = models.ForeignKey(Order, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    pieces     = models.PositiveIntegerField()
    total      = models.PositiveIntegerField()
