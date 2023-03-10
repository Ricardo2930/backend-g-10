from models.categorias_model import CategoriasModel
from db import db
import pandas
from flask import send_file

#class o constructor
class CategoriasController:
    def  __init__(self) -> None:
        self.model = CategoriasModel

    def crearCategoria (self, data):
        try:
            categoria = self.model(data['nombre'])
            db.session.add(categoria)
            db.session.commit()
            return {
                'data': categoria.convertirJson()
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def listarCategorias(self, id):
        try:
            print(id)
            categorias = self.model.query.all()
            #categorias = self.model.query.filter_by(estado=True).all()
            response = []
            for categoria in categorias:
                response.append(categoria.convertirJson()) #Es lo mismo que las 3 líneas de abajo
            # response = [
            #     categoria.convertirJson()
            #     for categoria in categorias
            # ]
                
            return {
                'data': response
            }, 200
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def actualizarCategoria(self, categoria_id, data):
        try:
            categoria = self.model.query.get(categoria_id)
            categoria.nombre = data['nombre']
            db.session.commit()
            return {
                'data': categoria.convertirJson()
            }
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def eliminarCategoria(self, categoria_id):
        try:
            categoria = self.model.query.get(categoria_id) #primary key
            categoria.estado = False
            db.session.commit()
            return {
                'data': categoria.convertirJson()
            }
        except Exception as e:
            db.session.rollback() # se usa en transacciones 
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
    
    def importarExcel (self):
        try:
            #LINEAS DE CODIGO PARA CREAR UN EXCEL 
            categorias = self.model.query.all()
            dct = {
                'Name': {
                    0: 'Ram',
                    1: 'Deep', 
                    2: 'Yash',
                    3: 'Aman', 
                    4: 'Arjun',
                    5: 'Aditya', 
                    6: 'Divya',
                    7: 'Chalsea', 
                    8: 'Akash' 
                }
            }
            data = pandas.DataFrame(dct)
            data.to_excel("output.xlsx")
            return send_file('output.xlsx', download_name='Adjacency.csv')
        
            #LINEAS DE CODIGO PARA LEER UN EXCEL 
            # documento = pandas.read_excel ('alumnos.xlsx',sheet_name='Hoja1')
            # #print (documento)
            # response = []
            # for alumno in documento['alumno']:
            #     response.append ({
            #         'nombre' : alumno,
            #     })
            # return {
            #     'data' : response
            # },200
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
        