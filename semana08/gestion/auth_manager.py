from django.contrib.auth.models import BaseUserManager

# BaseUserManager, sirve para modificar la creacion y administracion de los auth_user

class UsuarioManager (BaseUserManager):
    # Esta clase me permitira modificar la administracion del usuario mediante el comando creatwsuperuser
    def create_superuser (self, correo, nombre, apellido, tipoUsuario, password):
        
        # Valido si es que no hay correo
        if not correo:
            raise ValueError('El usuario no proporciono correo')
        
        # Valido que el correo cumpla con el formato correcto
        # Removera los espacios al incio y al final y validara que no se utilice caracteres incorrectos
        correo_normalizado = self.normalize_email(correo)
        
        #Llamamos al modelo que estamos utilizando AUTH_USER e inicializamos el nuevo usuarios con ()
        nuevo_usuario = self.model(correo=correo_normalizado, nombre = nombre, apellido=apellido, tipoUsuario=tipoUsuario) 

        # Generamos el hash de la contraseña
        # Generar el hash de la contraseña utilizando algoritmos de hash SHA512
        # https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password
        nuevo_usuario.set_password(password)

        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True

        nuevo_usuario.save()