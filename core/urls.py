from django.urls import path
from .views import *

urlpatterns= [
    path('home',home,name="home"),
    path('', root),
    path('productos',productos,name="productos"),
    path('ayuda',ayuda,name="ayuda"),
    path('micuenta',micuenta,name="micuenta"),
    path('compraproductos',compraproductos,name="compraproductos"),
    path('despacho',despacho,name="despacho"),
    path('formasdepago',formasdepago,name="formasdepago"),
    path('preguntasfrecuentes',preguntasfrecuentes,name="preguntasfrecuentes"),
    path('registro',registro,name="registro"),
    path('iniciarsesion',iniciarsesion,name="iniciarsesion"),
    path('cuenta',cuenta,name="cuenta"),
    path('ofertas',ofertas,name="ofertas"),
    path('terminosycondiciones',terminosycondiciones,name="terminosycondiciones"),
    path('afiliados',afiliados,name="afiliados"),
    path('nuestrosdescuentos',nuestrosdescuentos,name="nuestrosdescuentos"),
    path('trabajeconnosotros',trabajeconnosotros,name="trabajeconnosotros"),
    path('atencionlocales',atencionlocales,name="atencionlocales"),
    path('vistasucursales',vistasucursales,name="sucursales"),
    path('carnet_tipo3',carnet_tipo3,name="carnet_tipo3"),
    path('cascabel_gato',cascabel_gato,name="cascabel_gato"),
    path('bandana_perro',bandana_perro,name="bandana_perro")

]