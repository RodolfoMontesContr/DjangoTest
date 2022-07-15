from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('',editarsucursales,name='editarsucursales')
]