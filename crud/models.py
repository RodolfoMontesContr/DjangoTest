from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    precio= models.PositiveSmallIntegerField()

    def __str__(self):
        texti = "{0} ({1})"
        return texti.format(self.nombre,self.precio)

class Marca(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    
    
class Categoria(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    
    
class Distribuidora(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    
class Usuario(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    
