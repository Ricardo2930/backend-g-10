from flask import Flask
#si el archivo es eñ archivo principal del proyecto su valor de la variable __name__ sera '__main__' caso contrario sera none (vacio)
app = Flask (__name__)
#una sola instancia de clase 
#patron de diseño de software (singleton) 

#un decorador se usa con el @ y sirve para modificar cierto metodo de una clase sin la necesidad de modificar el funcionamiento natural (es una modificacion parcial) luego de utilizar el decorador se crea una funcion que sera la nueva funcionalidad de ese metodo 
@app.route('/')

def inicio ():
    return 'Hola desde mi servidor de Flask'

@app.route('/mostrar-hora', methods=['GET','POST'])

def mostrarHora ():
    #no se suele retornar strings (cadena de texto) sino que se utiliza diccionario
    return {'content':'22:50:25'}




#
app.run (debug=True)


