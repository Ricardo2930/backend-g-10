from flask import Flask,render_template
from os import environ
from dotenv import load_dotenv
load_dotenv()


app = Flask (__name__)

@app.route("/")
def inicio ():
    return"""
    <p>
    Hola desde back
    </p>
    <h1>
    Hola
    </h1>
    """

@app.route("/productos")
def productos ():
    #consumir la BD para devolver los productos
    lista_productos = [
        {
            'id':1,
            'nombre':'coliflor',
            'precio':4.50
        },
        {
            'id':2,
            'nombre': 'berengena',
            'precio': 5.80
        },
        {
            'id':3,
            'nombre':'platano de seda',
            'precio': 4.70
        }
    ]
    return render_template("listar_productos.html", nombre='Ricardo', lista_productos=lista_productos)

app.run(debug=True)