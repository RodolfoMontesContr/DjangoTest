from django.urls import URLPattern, path
from .views import *
from .import views

urlpatterns = [
    path('',editarsucursales,name='editarsucursales'),
    path('new/',nueva_sucursal,name='nueva-sucursal'),
    path('borrar_sucursal/<sucursal_id>', views.borrar_sucursal),
    path('editar_sucursal/<sucursal_id>',editar_sucursal,name='sucursal_edicion'),
]