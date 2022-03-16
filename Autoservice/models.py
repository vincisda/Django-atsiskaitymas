from django.db import models

# Create your models here.
class Car(models.Model):
    state_registration = models.CharField(max_length=20, null=False )
    car_model_id       = models.CharField(max_length=100) 
    vin_code           = models.CharField(max_length=30)
    client             = models.CharField(max_length=100)


class CarModel(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100) 
