from models.usuarios_model import UsuariosModel
from db import db

class UsuariosController:
    def __init__(self) -> None:
        self.model = UsuariosModel

    def crearUsuario(self, data):
        try:
            contraseña = self.__encriptarContraseña (data ['contraseña'])
            usuario = UsuariosModel(data['nombres'], data['correo'], data ['imagen'], contraseña)
            db.session.add(usuario)
            db.session.commit()
            return {
                'data' : usuario.convertirJson()
            }    
        
        except Exception as e:
            return {
                'message' : 'Internal server error',
                'error' :str(e)
            },500

    def __encriptarContraseña (self, contraseña):
        contraseña_encriptada = ""
        return contraseña_encriptada