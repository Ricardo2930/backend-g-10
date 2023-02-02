from models.usuarios_model import UsuariosModel
from werkzeug.security import generate_password_hash, check_password_hash
from db import db

class UsuariosController:
    def __init__(self) -> None:
        self.model = UsuariosModel

    def crearUsuario(self, data):
        try:
            contraseña = self.__encriptarContraseña (data ['contraseña'])
            #print(contraseña) -> self.model = UsuariosModel
            usuario = self.model(data['nombres'], data['correo'], data ['imagen'], contraseña)
            db.session.add(usuario)
            db.session.commit()
            return {
                'data' : usuario.convertirJson()
                #'data' : 'Contraseña Encriptada'
            }    
        
        except Exception as e:
            return {
                'message' : 'Internal server error',
                'error' :str(e)
            },500

    def __encriptarContraseña (self, contraseña):
        return generate_password_hash (contraseña)