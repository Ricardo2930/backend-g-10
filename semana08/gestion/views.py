from rest_framework.generics import ListCreateAPIView
from .models import CategoriaModel
from .serializers import CategoriaSerializer
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