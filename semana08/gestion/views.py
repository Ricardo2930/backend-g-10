from rest_framework.generics import ListCreateAPIView
from .models import CategoriaModel, PlatoModel
from .serializers import CategoriaSerializer, PlatoSerializer
from rest_framework.response import Response
from rest_framework.request import Request

#List - Listar (get)
#Create - Crear (post)
class CategoriaApiView(ListCreateAPIView):
    #al utilizar una vista generica que ya no es necesario definir el comportamiento paara cuando sea get o post
    #queryset -> El comando que utilizara para llamar a la informacion de nuestra base de datos
    #SELCT * FROM categoria:
    queryset = CategoriaModel.objects.all()

    # serializer_class -> Se define una clase qeu se encargara de convertir y transformar la informacion que viene desde el cliente y la informacion que enviamos hacia el cliente en datos legibles
    
    serializer_class = CategoriaSerializer

    #ya no es necesario definir los metodos get y post
    # def get(self):
    #     pass

    # def post(self):
    #     pass

class PlatoApiView (ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer

    #Definimos el def GET para no sobreusar los generics, para poner la logica que queramos
    def get (self,request:Request): #variable de la clase :Request
        # Al colocar ':' indicamos que el tipo de dato que sera esa variable en el caso de que no la hemos seteado correctamente
        #request -> Toda la informacion que viene del cliente

        #SELECT*FROM platos WHERE disponibilidad = True
        resultado = PlatoModel.objects.filter(disponibilidad=True).all()
        print(resultado)
        return Response (data = {
            'message':'Me hizo get'
        })
