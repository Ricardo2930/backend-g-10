from os import listdir
from pathlib import Path

path_parent = Path("./routers")

for module in listdir(path_parent): #con listdir hacermos que nos liste todos los archivos de la carpeta routers
    if 'router' in module: #filtramos, comprobamos que exista la palabra router en esa carpeta (module) in listdir
        __import__( # IMPORTAMOS --- f' -> es introducit una variable en un string
            f'routers.{module[0:-3]}', #recorrer un string[0:-3] -- Ej. python[0:2]//pyt
            locals(), #importamos de modo local
            globals() #importamos de modo global
        )