from importlib.resources import path
from django import views
from django.urls import path
from . import views

urlpatterns = [

    path('', views.homeCategorias),
    path('registrarCategoria/', views.registrarCategoria),
    path('edicionCategoria/<codigo>', views.edicionCategoria),
    path('editarCategoria/', views.editarCategoria),
    path('eliminarCategoria/<codigo>', views.eliminarCategoria)
    
]
