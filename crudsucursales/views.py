from multiprocessing import context
from django.shortcuts import render, redirect, reverse

from crudsucursales.forms import SucursalForm
from .models import *

# Create your views here.


def editarsucursales(request):
    context = {'sucursal':Sucursal.objects.all()}
    return render(request,'crudsucursales/editarsucursales.html', context)

def nueva_sucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            idSucursal = form.cleaned_data.get("idSucursal")
            nombresucursal = form.cleaned_data.get("nombresucursal")
            direccion = form.cleaned_data.get("direccion")
            horario = form.cleaned_data.get("horario")
            festivos = form.cleaned_data.get("festivos")
            obj = Sucursal.objects.create(
                idSucursal=idSucursal,
                nombresucursal=nombresucursal,
                direccion=direccion,
                horario=horario,
                festivos=festivos
            )
            obj.save()
            return redirect(reverse('editarsucursales') + "?OK")
        else:
            return redirect(reverse('editarsucursales') + "?FAIL")
    else:
        form = SucursalForm
    return render(request,'crudsucursales/nueva-sucursal.html',{'form':form})



def borrar_sucursal(request,sucursal_id):
        sucursal = Sucursal.objects.get(idSucursal=sucursal_id)
        sucursal.delete()
        return redirect(reverse('editarsucursales'))

def editar_sucursal(request,sucursal_id):
    try:
        sucursal = Sucursal.objects.get(idSucursal=sucursal_id)
        form = SucursalForm(instance=sucursal)

        if request.method == 'POST':
            form = SucursalForm(request.POST,request.FILES,instance=sucursal)
            if form.is_valid():
                form.save()
                return redirect(reverse('editarsucursales') + '?UPDATED')
            else:
                return redirect(reverse('editar_sucursal') + sucursal_id)

        context = {'form':form}
        return render(request,'crudsucursales/sucursal_edicion.html',context)
    except:
        return redirect(reverse('editarsucursales') + "?NO_EXITS")