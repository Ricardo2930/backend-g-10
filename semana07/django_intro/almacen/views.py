from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductosModel, CategoriasModel
from .serializers import ProductosSerializer
from rest_framework import generics
from rest_framework.response import Response

def renderHtml(request):
    return HttpResponse("<button>Dame click</button>") # podemos devolver pero creando rutas urlpatterns

def buscarProducto(request, producto_id):
    producto = ProductosModel.objects.filter(id=producto_id).first() #objects ->
    return HttpResponse(f'El producto encontrado se llama {producto.nombre} y el precio es: {producto.precio}') # f' para dar formaro al string ''

class ProductosView(generics.ListCreateAPIView):
    queryset = ProductosModel.objects.all() #si o si va queryset (palabra reservada) #metodo all para llamar a todos los datos del modelo
    serializer_class = ProductosSerializer #si o si va serializer_class (palabra reservada)
    #con el objetcs hacemos referencia a todas las categorias (objetcs) para traerlos

# Por cada modelo, serializers creamos se crea una vista
class CategoriasView(generics.GenericAPIView): #los generics se trabajan con clases
    queryset = CategoriasModel.objects.all() #este metodo extrae todos los datos
    serializer_class = ProductosSerializer

    # Empezamos a definir los metodos GET, POST, ...
    def get(self,request):
        try:
            record = self.get_queryset()
            #print(record)
            serializer = self.get_serializer(record, many = True) # se le pasa la propiedad MANY para indicarle que es una lista. Y los modelos los pasa serializados
            return Response (serializer.data)
        except Exception as e:
            return Response ({
                'message' : 'Internal server error',
                'error' : str(e)
            })

    def post(self, request):
        try:
            categoria = self.get_serializer(data=request.data)
            if categoria.is_valid():
                categoria.save()
                print(categoria.data)
                return Response(categoria.data)
            return Response({
                
            })
        except:
            return Response({
                'message': 'Internal server error'
            })