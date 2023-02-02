from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from db import db
from flask_jwt_extended import JWTManager

app = Flask(__name__) #Es la instancia de Flask, nuestra app va a girar alrededor de app
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config["JWT_SECRET_KEY"] = "super-secret" #esta firma tiene que ser unica. Se ubica en una variable de entorno
jwt = JWTManager(app)

db.init_app(app)

migrate = Migrate(app,db)

@app.route("/") #Se define la ruta para cualquier consulta http
def index ():
    return "Mi aplicacion con Flask :D"



import routers

#if __name__ == '__main__':
#   app.run (debug=True) # Para que corra la app