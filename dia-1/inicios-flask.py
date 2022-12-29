from flask import Flask, request
from flask_cors import CORS
#si el archivo es el archivo principal del proyecto su valor de la variable __name__ sera '__main__' caso contrario sera none (vacio)
app = Flask (__name__)
#una sola instancia de clase 

#ahora configuramos nuestros CORS (Control de Acceso de Recursos Cruzados)
CORS(app=app, origins=['http://127.0.0.1:5500'], methods=['GET','POST'])

#patron de diseño de software (singleton) 

#creamos la variable USUARIOS =[]
usuarios = [
    {
        'nombre':'Eduardo',
        'apellido':'Juarez'
    },
    {
        'nombre':'Juana',
        'apellido':'Rodriguez'
    },
    {
        'nombre':'Roberto ',
        'apellido':'Castillo'
    }
]

#un decorador se usa con el @ y sirve para modificar cierto metodo de una clase sin la necesidad de modificar el funcionamiento natural (es una modificacion parcial) luego de utilizar el decorador se crea una funcion que sera la nueva funcionalidad de ese metodo 
@app.route('/')

def inicio ():
    return 'Hola desde mi servidor de Flask'

#END POINT (punto final) declaración de la finalizacion de la url que indicara que accion se debe realizar
@app.route('/mostrar-hora', methods=['GET','POST'])

def mostrarHora ():
    #CONTROLLER (controlaor) es una funcionalidad que se realiza dentro de un determinado endpoint
    #request -- me dara toda la informacion que viene desde el cliente
    print (request.method)
    if request.method == 'GET':
        return {
            'content':'Me hiciste GET'
        }
    elif request.method == 'POST':
        return {
            'content':'Me hiciste POST'
        }

    #no se suele retornar strings (cadena de texto) sino que se utiliza diccionario
    return {'content':'22:50:25'}

@app.route ('/usuarios', methods=['GET','POST'])
def gestionUsuario ():
    if request.method == 'GET':
        #devolveremos los usuarios
        return {
            'message':'Los usuarios son',
            'content': usuarios
        }
    elif request.method == 'POST':
        #agregar un nuevo usuario
        #request.data -- mostrara la info proveniente del body en formato bytes
        #request.get_json() > convierte el body entrante en un diccionario desde un JSON
        print(request.get_json())
        data = (request.get_json())
        #con append se agrega data a nuestro arreglo Usuarios
        usuarios.append(data)
        return {
            'message':'usuario agregado exitosamente'
        }

# debug = cada vez que modifiquemos algun archivo del proyecto y guardamos, se reiniciara el servidor
app.run (debug=True)


