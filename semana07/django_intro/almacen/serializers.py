from rest_framework import serializers
from .models import ProductosModel, CategoriasModel

# serializador darle formato a los datos a devolver, y controla los campos que se van a enviar (POST)
class ProductosSerializer(serializers.ModelSerializer): # () Ahi dentro se hereda la clase 
    estado = serializers.BooleanField(read_only=True)
    class Meta:
        model = ProductosModel #modelo a serializar
        # fields = ['nombre', 'precio']
        fields = '__all__' #campos a serializar del modelo
        # exclude = ['estado']

#Por cada modelo creado, creamos su serializers
class CategoriasSerializer (serializers.ModelSerializer):
    class Meta:
        model = CategoriasModel
        fields = '__all__'