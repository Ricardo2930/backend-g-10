from rest_framework import serializers
from .models import ProductosModel, CategoriasModel, ClientesModel,OrdenesModel, DetallesOrdenModel

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

    def delete(self):
        self.instance.estado = False
        self.instance.save()

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientesModel
        fields = '__all__'

class DetallesOrdenSerializer(serializers.ModelSerializer):
    class Meta :
        model = DetallesOrdenModel
        fields = ['cantidad','producto_id']
class OrdenesSerializer (serializers.ModelSerializer):
    cliente = ClientesSerializer(source ='id')
    detalle = DetallesOrdenSerializer(many = True, write_only =True)
    class Meta:
        model = OrdenesModel
        exclude = ['estado','cliente_id']

class GetOrdenesSerializer(serializers.ModelSerializer):
    #cliente = ClientesSerializer (source = 'id')
    class Meta:
        model = OrdenesModel
        fields = '__all__'

# class DetallesOrdenSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = DetallesOrdenModel
#         fields = '__all__'

# class PagosSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = OrdenesModel
#         fields = '__all__'