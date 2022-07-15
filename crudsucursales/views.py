from django.shortcuts import render
from .models import *

# Create your views here.


def editarsucursales(request):
    return render(request,'crudsucursales/editarsucursales.html')

