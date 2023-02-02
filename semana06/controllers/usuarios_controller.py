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

    def iniciarSesion(self, data):
        try:
            
            usuario = self.model.query.filter_by(correo=data['correo']).first() #vamos a buscar al usuario (filtrar)
            print(usuario)
            if not usuario: #para validar el correo y contraseña que existan y sean las correctas
                return {
                    'message' : 'Unauthorized'
                },401
            print (self.__comprobarContraseña(data['contraseña'], usuario.contraseña))
            return {
                'access_token':'Esta es una token'
            }
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
    
    def __comprobarContraseña(self, contraseña, contra_hash):#contraseña hasheada, traiada desde la BD
        return check_password_hash(contraseña, contra_hash)

    def __encriptarContraseña (self, contraseña):
        return generate_password_hash (contraseña)