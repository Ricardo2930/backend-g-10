from app import app
from controllers.categorias_controller import CategoriasController
from flask import request


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


@app.route("/categorias/listar", methods=['GET'])
def categoriasListar():
    controller = CategoriasController()
    return controller.listarCategorias()