from rest_framework import serializers
from crud.models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields =(
            'codigo','nombre','precio'
        )
    

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Marca
        fields=(
            'codigo','nombre'
        )