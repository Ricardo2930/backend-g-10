from rest_framework import serializers
from .models import CategoriaModel, PlatoModel

class CategoriaSerializer(serializers.ModelSerializer):
    # cuando utilizamos un serializador basandonos en un modelo se declara la clase Meta
    class Meta:
        # este se encargara de mapear todos los atributos del modelo para hacer concordar el tipo de dato y sus especificaciones
        model = CategoriaModel
        # fields > sirve para indicar que columnas de esa tabla queremos trabajar, si queremos todas las columnas entonces definiremos el valor de '__all__' caso contrario lo podremos manejar en un arreglo con los nombre de las columnas
        fields = '__all__'
        # fields = ['id', 'nombre']
        # si queremos excluir una minima cantidad de columnas para no trabajarlas entonces usaremos 
        # exclude = ['id']
        
        # NOTA: no se puede trabajar con el exclude y el fields a la vez, o es uno o es el otro

class PlatoSerializer (serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        exclude = ['disponibilidad'] #excluimos el atributo disponibilidad
         # Este atributo sirve para poder conectarnos a las relaciones adyacentes a este modelo, que tan profundidad quieres ingresar, sube un nivel si es 1 y asi sucesivamente.
        #Sirve solamente para tablas en las cuales tengamos una llave foranea, es decir que esta tabla dependa de otra.
        # Sirve para decirle que desde el plato nos podamos mover un nivel hacia arriba y devolver lo que vendria a ser la categoria.
        depth = 1

class CategoriaConPlatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'
       