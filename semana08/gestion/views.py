from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView
from .models import CategoriaModel, PlatoModel
from .serializers import CategoriaSerializer, CategoriaConPlatosSerializer, MostrarPlatoSerializer, CrearPlatoSerializer
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
    #serializer_class = PlatoSerializer --> Cuando nosotros modificamos la funcionalidad de los metodos ya no es necesario definir los atributos obligatorios (y queryset)

    #Definimos el def GET para no sobreusar los generics, para poner la logica que queramos
    def get (self,request:Request): #variable de la clase :Request
        # Al colocar ':' indicamos que el tipo de dato que sera esa variable en el caso de que no la hemos seteado correctamente
        #request -> Toda la informacion que viene del cliente

        #SELECT*FROM platos WHERE disponibilidad = True
        resultado = PlatoModel.objects.filter(disponibilidad=True).all()
        print(resultado)
        # Aca llamamos a serializer y le pasamos la informacion proveniente de la BD y con el parametro many=True indicamos que le estamos pasando un arreglo de instancias
        serializador = MostrarPlatoSerializer(instance = resultado, many=True)
        print (serializador.data)
        return Response (data = {
            'message':serializador.data
        })

    def post (self, request:Request):
        body = request.data #Me devuelve la info del BODY
        # Cuando queremos verificar si la informacion entrante es valida entonces utilizamos el parametro DATA en vez del paramentro instance
        serializador = CrearPlatoSerializer(data = body) # (parametro del serial = data que es iguak a request.data)
        # Es el encargado de validar si la data es correcta y cumple con todos los requisitos
        #Instanciar, tomo toda la configuracion o copia de una clase y la uso en la variable guardada 
        valida = serializador.is_valid()

        platoExistente = PlatoModel.objects.filter(nombre = body.get('nombre')).first()

        if platoExistente:
            return Response(data = {
                'message':'El plato con nombre {} ya existe'.format(platoExistente.nombre)
            })

        if valida == False:
            return Response (data = {
                'message':'La informacion es invalida',
                #error > Mostrar los errores SOLAMENTE cuando la data es invalida
                'content':serializador.errors # Argumento (atributo) de la clase definidos 
            })

        # si la data pasada al serializador es una data valida entonces esta informacion se guardara en el atributo validated_data que es un diccionario, el validated_data solamente estara disponible cuando mandemos a la validacion, si no se hace la validacion el validated_data sera vacio
        # platoExistente = PlatoModel.objects.filter(nombre = serializador.validated_data.get('nombre')).first()

        # if platoExistente : 
        #     return Response(data={
        #         'message': 'El plato con nombre {} ya existe'.format(platoExistente.nombre)
        #     })

        print(serializador.validated_data)
        # Asi guardamos la informacion en la base de datos utilizando el serializador save()
        nuevoPlato = serializador.save() #save() es un metodo de serializador
        print(nuevoPlato)
        serializar = MostrarPlatoSerializer (instance=nuevoPlato) #instance es el parametro
        return Response (data = {
            'message':'Plato creado exitosamente',
            #method data > Es la informacion convertida a un diccionario para que pueda ser entendida por el cliente
            'content':serializar.data
        })

class PlatoDestroyApiView(DestroyAPIView):
    # queryset = PlatoModel.objects.all()
    # serializer_class = PlatoSerializer

    def delete(self, request: Request, pk: int):
        print(pk)
        platoEncontrado = PlatoModel.objects.filter(id = pk, disponibilidad = True).first()

        if platoEncontrado is None:
            return Response(data={
                'message': 'El plato no existe'
            })
        
        # Le cambiamos la disponibilidad
        platoEncontrado.disponibilidad = False
        
        # guardamos los cambios en la bd
        platoEncontrado.save()

        return Response(data={
            'message': 'Plato eliminado exitosamente'
        })

    
class ListarCategoriasApiView(ListAPIView):
    def get(self, request:Request, pk:int):
        categoriaEncontrada = CategoriaModel.objects.filter (id = pk).first()
        print (categoriaEncontrada)
        if categoriaEncontrada is None:
            return Response(data={
                'message':'Categoria no existe'
            })
        #dir(instancia) -> Nos muestra todos los atributos t metodos de la clase
        #print(dir(categoriaEncontrada))

        print (categoriaEncontrada.platos.all())
        plato = categoriaEncontrada.platos.all()[1]
        print(plato.nombre)
        serializador = CategoriaConPlatosSerializer(instance = categoriaEncontrada)

        return Response(data= {
            'content':serializador.data
        }) 