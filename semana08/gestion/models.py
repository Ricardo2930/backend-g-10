from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth_manager import UsuarioManager

# Create your models here.
class CategoriaModel(models.Model):
    # Si no especificamos la columna ID, Django lo hara de manera predeterminada con el tipo de dato AutoField y tambien lo colocara como llave primaria
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types

    id = models.AutoField (primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True)# en la BD creara un varchar con 50 caracteres de longitud maxima

    class Meta:
        #Sirve para definir los atributos de la clase que estamos heredando directamente para pasarle la metadata sin utilizar el metodo SUPER
        #Metadatos, para modificar la configuracion y comportamiento de esta tabla en la base de datos
        # https://docs.djangoproject.com/en/4.1/ref/models/options/

        db_table = 'categorias'
        #modificamos el ordenamiento al momento de devolver los registros
        #nombre ascendente (a-z)
        #nombre descendente (z-a) ['-nombre']
        ordering = ['nombre', 'id'] #si tenemos nombres iguale, entra a ordenar por el ID

class PlatoModel(models.Model):
    #id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True, null=False)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    # auto_now_add > cada vez que cree un nuevo registro su valor sera la hora y fecha actual del servidor de base de datos por lo que ya no nos tenemos que preocupar en colocar la fecha 
    # db_column > indicar como se tiene que llamar esta columna en la base de datos solamente si queremos cambiar el nombre del atributo
    fechaCreacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    # Forma de indicar que accion debe tomar cuando se elimine el 'padre'
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    # CASCADE > Cuando se elimine una categoria en forma de cascada se eliminaran todos los platos
    # PROTECT > Evita la eliminacion de la categoria si esta tiene platos que dependan de ella, emitira un error ProtectedError
    # RESTRICT > Restinge la eliminacion, es lo mismo que el PROTECT solo que emitira un error de tipo RestrictedError
    # SET_NULL > permite la eliminacion de la categoria y a los platos que dependan de ella les cambiar su valor por NULL
    # SET_DEFAULT > permite la eliminacion de la categoria y les cambiar el valor a un valor por defecto
    # DO_NOTHING > permite la eliminacion PERO no hace nada osea mantiene el mismo numero de categoria en el plato a pesar que este no exista generando un problema de integridad 

    categoria = models.ForeignKey (to=CategoriaModel, on_delete=models.PROTECT,db_column='categoria_id',related_name='platos')
    #related_name=Sirve para acceder a todos los registros desde la otra entidad, es dewcir desde categoria poder acceder a todos sus platos, si es que no se define su valor sera puesto por Django con el nombre de la clase TODO EN MINUSCULAS seguido de la palabra_set 'platomodel_set'

    class Meta:
        db_table = 'platos'

# Como vamos a modificar el comportamiento de la tabla auth_user de Django entonces tenemos que modificar su herencia
class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    # PermissionsMixin -> Sirve para poder relacionar la tabla auth_user con las demas tablas de permisos, tanto la de auth_permission como la de group_permissions
    # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
    #AbstractBaseUser -> Me permite modificar todo lo que yo quiera del modelo auth_user mientras que el AbstracUser solo me permite agregar nuevas columnas

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50,null=False)
    apellido = models.CharField(max_length=50,null=False)
    # Django hace una validacion para que el correo cumpla con el formato válido xxxx@gmai.com
    correo = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(null=False)
    # CHOICES -> (Opciones), porque el primero es con el que se guardara en la base de datos, y el segundo es con que se mostrara al momento de devolver la informacion
    tipoUsuario = models.CharField(max_length=40, choices=[('ADMIN', 'ADMINISTRADOR') , ('MOZO','MOZO')])
    #enum -> o eres usuario o administrador
    #Propiedades Netas para el Panel Administrativo
        # Sirve para indicar si el usuario que quiere acceder pertenece o no al equipi de trabajo
    is_staff = models.BooleanField(default=False)

        # Sirve para indicar si el usuario es un usuario activo de la empresa
    is_active = models.BooleanField(default=True)

        # Sirve para indicar la fecha en la que se creo el usuario
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at') 

    # Propio del modelauth_user
    #Par el panel administrativo para indicar cual es el atributo que debe pedir como nombre de usuario
    USERNAME_FIELD='correo'

     # son las columnas o los atributos requeridos al momento de crear el superusuario por consola, no se coloca el username_field ni tampoco la contraseña porque ya son implicitos
    REQUIRED_FIELDS = ['nombre', 'apellido', 'tipoUsuario']

    objects = UsuarioManager()
    class Meta:
        db_table = 'usuarios'