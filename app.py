from flask import Flask
from os import environ
from configuracion import conexion
from dotenv import load_dotenv
from flask_migrate import Migrate

from models.categorias_model import Categoria
from models.productos_model import Producto
from models.categorias_productos_model import CategoriaProducto

# aca utilizaremos el archivo .env para agregarlo a las variables de entorno
load_dotenv()

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = environ.get ('DATABASE_URL')


# inicializamos la aplicacion de SQLAlchemy con nuestra apliacion de flask
conexion.init_app(app) # app es la aplicacion de flask

# Inicializamos la clase Migrate pasandole nuestra aplicacion de Flask y nuestra conexion a SQLAlchemy
Migrate(app,conexion)

# Asi utilizariamos la creacion de las tablas sin utilizar migraciones
# este controlador se ejecutara antes del primer request de nuestro servidor
# NOTA -- Tenemos que ir al postman y hacer un peticion para que se cree nuevas tablas
@app.before_first_request
def inicializadora():
    # realizar la creacion de todos los modelos de nuestro proyecto com tablas en la base de datos
    # antes de realizar la primera peticion, ejecutara esta funcion.
    #conexion.create_all()
    pass

if __name__ == '__main__':
    app.run (debug = True)
    