from flask import Flask,request
from flask_mysqldb import MySQL
#Devuelve todas las variables de entorno del dispositivo
from os import environ

from dotenv import load_dotenv
load_dotenv()

app = Flask (__name__)
#Toda esta configuracion es para conectarme a mi base de datos
#Cuando tenemos un diccionario podemos OBTENER el valor de una de las llaves con el metodo .get('LLAVE'), SOLO es para obtener, no es para asignar. Y si que al obtener no hay valor entonces colocara None (vacio)
# ESTO NO SE PUEDE HACER:
# environ.get('MYSQL_HOST') = 'hola'
# environ['MYSQL_HOST']='hola'
app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = int(environ.get('MYSQL_PORT')) #con INT convetimos este valor a entero

#Cuando a una vbariables se le asigna una clase se llama INSTANCIA
#inicializamos la conexion seteando todos los parametros de nuestra DB, PERO AUN NO NOS CONECTAMOS
mysql = MySQL(app)

#REQUEST devuelve toda la informacion del cliente
@app.route('/productos',methods=['GET','POST'])
def gestion_productos():
    if request.method == 'GET':
        #cursor, crea una conexion a la BD mediante un cursor
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM PRODUCTOS")
        productos = cursor.fetchall() #limit infinite
        # cursor.fetchone() limit1
        print (productos)
        #cerrar nuestra conexion
        cursor.close()

        return {
            'message':'los productos son'
        }
    elif request.method == 'POST':
        return {
            'message':'producto creado exitosamente'
        }


# load_dotenv - cargamos todas las variables definidas en el archivo .env como variables de entorno, todas estas variables siempre son STRING
app.run(debug=True, load_dotenv=True)