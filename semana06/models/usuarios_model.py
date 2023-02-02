from db import db
from sqlalchemy import Column, String, Integer, Text

class UsuariosModel (db.Model):
    __tablename__ = "usuarios"

    id = Column (Integer, primary_key = True, autoincrement = True)
    nombres = Column ( String(200), nullable = False)
    correo = Column (String(100), nullable = False)
    imagen = Column (Text, nullable = True)
    contraseña = Column (Text, nullable =False)

    def __init__(self, nombres, correo, imagen, contraseña) -> None:
        self.nombres = nombres
        self. correo = correo
        self. imagen = imagen
        self. contraseña = contraseña

    def __str__(self) -> str: #metodo magico para no retorne UsuarioModel1 sino el nombre asignado
        return self.nombres

    def convertirJson (self):
        return {
            'id' : self.id,
            'nombres' : self.nombres,
            'correo' : self.correo,
            'imagen' : self.imagen,
        }
