from django import forms
from django.forms import ModelForm
from .models import *

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = [
            'idSucursal',
            'nombresucursal',
            'direccion',
            'horario',
            'festivos'
        ]
        labels = {
            'idSucursal':'ID Sucursal',
            'nombresucursal': 'Nombre de la sucursal',
            'direccion': 'Dirección',
            'horario': 'Horario',
            'festivos': 'Festivos'
        }
        widgets = {
            'idSucursal':forms.TextInput(attrs={'class':'form-control'}),
            'nombresucursal':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'horario':forms.TextInput(attrs={'class':'form-control'}),
            'festivos':forms.TextInput(attrs={'class':'form-control'})
        }
