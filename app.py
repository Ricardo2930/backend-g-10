from flask import Flask
from os import environ
from configuracion import conexion
from dotenv import load_dotenv

from models.categorias_model import Categoria

# aca utilizaremos el archivo .env para agregarlo a las variables de entorno
load_dotenv()

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = environ.get ('DATABASE_URL')

# inicializamos la aplicacion de SQLAlchemy con nuestra apliacion de flask
conexion.init_app(app) # app es la aplicacion de flask

# este controlador se ejecutara antes del primer request de nuestro servidor
@app.before_first_request
def inicializadora():
    # realizar la creacion de todos los modelos de nuestro proyecto com tablas en la base de datos
    # antes de realizar la primera peticion, ejecutara esta funcion.
    conexion.create_all()

if __name__ == '__main__':
    app.run (debug = True)
    