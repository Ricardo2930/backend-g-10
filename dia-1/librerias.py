#Importando la libreria CamelCase
from camelcase import CamelCase

#Iniciar una variable, llamar una variable con sus metodos, funciones, etc para ser usado-
#Instancia = agarrar un clase en una variable para usarlo, y todas las modificaciones solo quedan ahi dentro
instancia = CamelCase()
otraInstancia = CamelCase()

texto = 'hola yo deberia estar camel caseado'

resultado = instancia.hump (texto)

print (resultado)
