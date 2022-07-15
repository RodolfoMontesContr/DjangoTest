from mailbox import NoSuchMailboxError
from django.shortcuts import render , redirect
from .models import Categoria

# Create your views here.

def homeCategorias(request):
    categoriasListados = Categoria.objects.all()
    return render(request, "gestionCategorias.html", {"categorias": categoriasListados})

def registrarCategoria(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    

    categoria=Categoria.objects.create(
        codigo=codigo, nombre=nombre)
    return redirect('/')

def edicionCategoria(request, codigo):
    categoria = Categoria.objects.get(codigo = codigo)
    return render(request,"edicionCategorias.html", {"categoria": categoria})

def editarCategoria(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    

    categoria = Categoria.objects.get(codigo = codigo)
    categoria.nombre = nombre
    
    categoria.save()
    return redirect('/')


def eliminarCategoria(request , codigo):
    categoria = Categoria.objects.get(codigo = codigo)
    categoria.delete()
    return redirect('/')