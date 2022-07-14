from msilib.schema import AppId
from nturl2path import url2pathname
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,'core/home.html')

def root(request):
    return redirect('/home')

def productos(request):
    return render(request,'core/productos.html')

def ayuda(request):
    return render(request,'core/ayuda.html')

def micuenta(request):
    return render(request,'core/micuenta.html')

def compraproductos(request):
    return render(request,'core/compraproductos.html')

def despacho(request):
    return render(request,'core/despacho.html')

def formasdepago(request):
    return render(request,'core/formasdepago.html')

def preguntasfrecuentes(request):
    return render(request,'core/preguntasfrecuentes.html')

def registro(request):
    return render(request,'core/registro.html')

def iniciarsesion(request):
    return render(request,'core/iniciarsesion.html')

def cuenta(request):
    return render(request,'core/cuenta.html')

def ofertas(request):
    return render(request,'core/ofertas.html')

def terminosycondiciones(request):
    return render(request,'core/terminosycondiciones.html')

def afiliados(request):
    return render(request,'core/afiliados.html')

def atencionlocales(request):
    return render(request,'core/atencionlocales.html')

def nuestrosdescuentos(request):
    return render(request,'core/nuestrosdescuentos.html')

def trabajeconnosotros(request):
    return render(request,'core/trabajeconnosotros.html')
