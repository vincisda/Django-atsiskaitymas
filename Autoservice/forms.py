from django import forms

from .models import Car, CarModel, Service, OrderRow, Order



class CarForm(forms.ModelForm):
    class Meta:
        model  = Car
        fields = [
            'state_registration', 'vin_code', 'client',
        ]

class RawCarForm(forms.Form):
    state_registration = forms.CharField()
    vin_code           = forms.CharField()
    client             = forms.CharField()