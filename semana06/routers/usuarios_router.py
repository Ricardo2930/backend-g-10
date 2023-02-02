from app import app
from controllers.usuarios_controller import UsuariosController
from flask import request

@app.route ("/auth/register", methods = ['POST'])
def usuariosRegister():
    controller = UsuariosController()
    return controller.crearUsuario(request.json) # request.json = data

@app.route("/auth/autenticar", methods=['POST'])
def usuariosAutenticar():
    controller = UsuariosController()
    return controller.iniciarSesion(request.json)