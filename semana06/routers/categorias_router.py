from app import app
from controllers.categorias_controller import CategoriasController
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route("/categorias/crear", methods=['POST'])
def categoriasCrear(): #definimos la funcion
    controller = CategoriasController() #nuestro contolador
    return controller.crearCategoria(request.json) #lo que se va a retornar


@app.route("/categorias/actualizar/<int:categoria_id>", methods=['PUT'])
def categoriasActualizar(categoria_id):
    controller = CategoriasController()
    return controller.actualizarCategoria(categoria_id, request.json)


@app.route("/categorias/eliminar/<int:categoria_id>", methods=['DELETE'])
def categoriasEliminar(categoria_id): #recibimos en la funcion
    controller = CategoriasController()
    return controller.eliminarCategoria(categoria_id) #lo enviamos al metodo

#Vamos a ptoteger esta ruta con jwt_required(). Para acceder en postman AUTHORIZATION - BEARER TOKEN - TOKEN 
@app.route("/categorias/listar", methods=['GET'])
@jwt_required()
def categoriasListar():
    user_id = get_jwt_identity()
    #print(user_id)
    controller = CategoriasController()
    return controller.listarCategorias(user_id)

@app.route("/categorias/importarxlsx", methods=['GET'])
def categoriasImportar():
    controller = CategoriasController()
    return controller.importarExcel()

