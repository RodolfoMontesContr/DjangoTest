from mailbox import NoSuchMailboxError
from django.shortcuts import render , redirect
from .models import Producto

# Create your views here.

def homeProductos(request):
    productosListados = Producto.objects.all()
    return render(request, "gestionProductos.html", {"productos": productosListados})

def registrarProducto(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    precio =request.POST['numPrecio']

    producto=Producto.objects.create(
        codigo=codigo, nombre=nombre,precio=precio)
    return redirect('/')

def edicionProducto(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    return render(request,"edicionProducto.html", {"producto": producto})

def editarProducto(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    precio =request.POST['numPrecio']

    producto = Producto.objects.get(codigo = codigo)
    producto.nombre = nombre
    producto.precio = precio
    producto.save()
    return redirect('/')


def eliminarProducto(request , codigo):
    producto = Producto.objects.get(codigo = codigo)
    producto.delete()
    return redirect('/')