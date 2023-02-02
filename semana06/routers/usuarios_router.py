from app import app
from controllers.usuarios_controller import UsuariosController
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request

@app.route ("/auth/register", methods = ['POST'])
def usuariosRegister():
    controller = UsuariosController()
    return controller.crearUsuario(request.json) # request.json = data

@app.route("/auth/autenticar", methods=['POST'])
def usuariosAutenticar():
    controller = UsuariosController()
    return controller.iniciarSesion(request.json)

@app.route("/auth/refresh", methods=['GET'])
@jwt_required(refresh = True)
def usuariosRefresh():
    identity = get_jwt_identity()
    controller = UsuariosController()
    return controller.refreshSesion(identity)