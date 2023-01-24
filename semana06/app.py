from flask import Flask
from flask_migrate import Migrate
from db import db

app = Flask(__name__) #Es la instancia de Flask, nuestra app va a girar alrededor de app

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

db.init_app(app)

migrate = Migrate(app,db)

@app.route("/") #Se define la ruta para cualquier consulta http
def index ():
    return "Mi aplicacion con Flask :D"



import routers

#if __name__ == '__main__':
#   app.run (debug=True) # Para que corra la app