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
        # Aca llamamos a serializer y le pasamos la informacion proveniente de la BD y con el parametro many=True indicamos que le estamos pasando un arreglo de instancias
        serializador = PlatoSerializer(instance = resultado, many=True)
        print (serializador.data)
        return Response (data = {
            'message':serializador.data
        })

    def post (self, request:Request):
        body = request.data #Me devuelve la info del BODY
        # Cuando queremos verificar si la informacion entrante es valida entonces utilizamos el parametro DATA en vez del paramentro instance
        serializador = PlatoSerializer(data = body) # (parametro del serial = data que es iguak a request.data)
        # Es el encargado de validar si la data es correcta y cumple con todos los requisitos
        #Instanciar, tomo toda la configuracion o copia de una clase y la uso en la variable guardada 
        valida = serializador.is_valid()

        if valida == False:
            return Response (data = {
                'message':'La informacion es invalida',
                #error > Mostrar los errores SOLAMENTE cuando la data es invalida
                'content':serializador.errors # Argumento (atributo) de la clase definidos 
            })
        
        # Asi guardamos la informacion en la base de datos utilizando el serializador save()
        nuevoPlato = serializador.save() #save() es un metodo de serializador
        print(nuevoPlato)
        serializar = PlatoSerializer (instance=nuevoPlato) #instance es el parametro
        return Response (data = {
            'message':'Plato creado exitosamente',
            #method data > Es la informacion convertida a un diccionario para que pueda ser entendida por el cliente
            'content':serializar.data
        })