from importlib.resources import path
from django import views
from django.urls import path
from . import views

urlpatterns = [

    path('', views.homeProductos),
    path('registrarProducto/', views.registrarProducto),
    path('edicionProducto/<codigo>', views.edicionProducto),
    path('editarProducto/', views.editarProducto),
    path('eliminarProducto/<codigo>', views.eliminarProducto)
    
]
