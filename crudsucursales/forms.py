from django import forms
from django.forms import ModelForm
from .models import *

class SucuralForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = [
            'idSucursal',
            'nombresucursal',
            'direccion'
        ]
        labels = {
            'idSucursal':'ID Sucursal',
            'nombresucursal': 'Nombre de la sucursal',
            'direccion': 'Dirección'
        }
        widgets = {
            'idSucursal':forms.TextInput(attrs={'class':'form-control'}),
            'nombresucursal':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'})
        }
