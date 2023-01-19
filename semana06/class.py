#Creamos un funcion con def
#Definimos la funcion
def miFuncionQueSuma (numero, otroNumero):
    resultado = numero + otroNumero
    print(resultado)
    return resultado
miFuncionQueSuma(10, 20); #LLamar o ejecutar la funcion

def multiplicar (a,b,c):
    return a*b*c
producto = multiplicar(3,3,3)
print(producto)

# Class es un objeto, y sus funciones dentro son metodos
class Operaciones:

    def suma(a,b):
        return a+b

    def multiplicar(a,b):
        return a*b

    def restar(a,b):
        return a-b

operacion = Operaciones
resultado = operacion.suma(5,10)
print(resultado)
    
resultado2=Operaciones.multiplicar(10,20)
print(resultado2)

#class con metodo magico
class Operaciones_2:
    def __init__(self, a, b): #init es el contructor
        self.primer_numero = a
        self.segundo_numero = b

    def restar(self):
        return self.primer_numero - self.segundo_numero

    def division(self):
        return self.primer_numero / self.segundo_numero        

#variable = class(objeto) (parametros)    
resultado_3= Operaciones_2 (50,20)
print (resultado_3.restar())
print (resultado_3.division())

# COMANDO PARA CREAR ENTRONO VIRTUAL --> 
# pyhton -m venv (nombre del entorno)
# source entorno_virtual/scripts/activate -- mac es /bin/ -- deactivate 

#pip install flask
#pip freese > requirements.txt
#pip install Flask-SQLAlchemy