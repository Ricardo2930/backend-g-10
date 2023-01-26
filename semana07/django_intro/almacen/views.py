from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductosModel
from .serializers import ProductosSerializer
from rest_framework import generics

def renderHtml(request):
    return HttpResponse("<button>Dame click</button>")

def buscarProducto(request, producto_id):
    producto = ProductosModel.objects.filter(id=producto_id).first()
    return HttpResponse(f'El producto encontrado se llama {producto.nombre} y el precio es: {producto.precio}') # f' para dar formaro al string ''

class ProductosView(generics.ListCreateAPIView):
    queryset = ProductosModel.objects.all() #si o si va queryset
    serializer_class = ProductosSerializer #si o si va serializer_class