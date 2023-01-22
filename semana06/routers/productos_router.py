from app import app
from controllers.productos_controll import ProductosController
from flask import request


@app.route("/productos",methods = ['GET']) # ruta para listar productos
def productos ():
    #return "Ruta productos"
    #CONTROLLER
    controller = ProductosController()
    return controller.listarProductos()

@app.route("/productos/crear", methods=['POST']) # ruta para crear productos
def productosCrear():
    controller = ProductosController()
    return controller.crearProducto(request.json) #() es la data

@app.route("/productos/eliminar/<int:producto_id>", methods=['DELETE']) # ruta para ELIMINAR productos
def productosEliminar(producto_id):
    controller = ProductosController()
    return controller.eliminarProducto(producto_id)

@app.route("/productos/actualizar/<int:producto_id>", methods=['PUT'])
def productosActualizar(producto_id):
    controller = ProductosController()
    return controller.actualizarProducto(producto_id, request.json)

@app.route("/productos/buscar/<float:precio>", methods=['GET'])
def productosBuscar(precio):
    controller = ProductosController()
    return controller.buscarProductos(precio)