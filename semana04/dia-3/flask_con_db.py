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

#Cuando a una variable se le asigna una clase se llama INSTANCIA
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
        # print (productos)
        #cerrar nuestra conexion
        cursor.close()
        resultado = []
        for producto in productos:
            producto_dic = {
                'id': producto[0],
                'nombre': producto[1],
                'imagen': producto[2],
                'fecha_vencimiento': producto[3].strftime('%Y-%m-%d'), # %H:%M:%S
                'precio': producto[4],
                'disponible': producto[5],
                'categoria_id': producto[6]
            }
            resultado.append(producto_dic)
            print(producto_dic)
        return {
            'message':'los productos son',
            'content':resultado
        }

    elif request.method == 'POST':
        cursor = mysql.connection.cursor()
        informacion = request.get_json() # un diccionario
        # %s > convierte el contenido a un string
        # %f > convierte el contenido a un numero flotante
        # %d > convierte el contenido a un numero entero
        cursor.execute("INSERT INTO productos (id, nombre, imagen, fecha_vencimiento, precio, disponible, categoria_id) VALUES (DEFAULT, '%s', '%s', '%s', %f, %s, %d)" % (
            informacion.get('nombre'),
            informacion.get('imagen'), 
            informacion.get('fecha_vencimiento'),
            informacion.get('precio'),
            informacion.get('disponible'),
            informacion.get('categoria_id')
            ))
        # indicamos que el guardado sea permanente en la base de datos
        mysql.connection.commit()
        cursor.close()
        return {
            'message':'producto creado exitosamente'
        }

def validar_producto(id):
    #creamos la conexion
        conexion = mysql.connection.cursor()
        #ejecutamos el SELECT con la clausula del ID
        conexion.execute(f"SELECT * FROM PRODUCTOS WHERE id={id}")#al poner la F antes del "", todo lo que esta en llaves el codigo python para que lo reconozca.
            #conexion.execute("SELECT * FROM PRODUCTOS WHERE id=%d"%(id))
            #conexion.execute("SELECT * FROM PRODUCTOS WHERE id="+str(id))
            #conexion.execute("SELECT * FROM PRODUCTOS WHERE id={}".format(id))
        resultado = conexion.fetchone()
        conexion.close()
        print(resultado)
        return resultado

@app.route("/producto/<int:id>", methods = ['GET', 'PUT', 'DELETE'])
def gestion_un_producto(id):
    if request.method == 'GET':
        resultado = validar_producto(id)
        if resultado is None:
            return {
                'message':'Producto no existe'
            }
        else:
            producto = {
                'id':resultado[0],
                'nombre':resultado[1],
                'imagen':resultado[2],
                'fecha_vencimiento':resultado[3].strftime('%Y-%m-%d'),
                'precio':resultado[4],
                'disponible':resultado[5],
                'categoria_id':resultado[6]
            }
        return {
            'content':producto
        }

    elif request.method=='PUT':
        resultado = validar_producto(id)
        if resultado is None:
            return {
                'message':'Producto no existe'
            }
        else:
            data=request.get_json()
            print(data)
            conexion=mysql.connection.cursor()
            conexion.execute("UPDATE productos SET nombre=%s, precio=%s, fecha_vencimiento=%s, categoria_id=%s, disponible=%s, imagen=%s WHERE id=%s",[
                data.get('nombre'),
                data.get('precio'),
                data.get('fecha_vencimiento'),
                data.get('categoria_id'),
                data.get('disponible'),
                data.get('imagen'),
                resultado [0]
            ])

            mysql.connection.commit()
            conexion.close()

            return {
                'message': 'Producto actualizado exitosamente'
            }

    elif request.method =='DELETE':
        resultado = validar_producto(id)
        if resultado is None:
            return {
                'message': 'Producto no existe'
            }

        else:
            conexion = mysql.connection.cursor()
            # primero eliminar ese producto en los almacenes
            conexion.execute("DELETE FROM productos WHERE id = %s", [id])
            mysql.connection.commit()
            conexion.close()

            return {
                'message': 'Producto eliminado exitosamente'
            }
    

# load_dotenv - cargamos todas las variables definidas en el archivo .env como variables de entorno, todas estas variables siempre son STRING
app.run(debug=True, load_dotenv=True)