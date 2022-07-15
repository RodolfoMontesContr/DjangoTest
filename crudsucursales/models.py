from django.db import models


# Create your models here.

class Sucursal(models.Model):
        idSucursal = models.CharField(primary_key=True,verbose_name='idSucursal', max_length=10)
        nombresucursal = models.CharField(verbose_name='NombreSucursal',max_length=30)
        direccion = models.CharField(verbose_name='Direccion',max_length=50)
        horario = models.CharField(verbose_name='Horario',max_length=50)
        festivos = models.CharField(verbose_name='Festivos',max_length=50)

class Meta:
        verbose_name = 'sucursal'
        verbose_name_plural = 'sucursales'