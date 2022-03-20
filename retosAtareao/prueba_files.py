#import mimetypes
#from os import *
import re


"""ruta2 = "/TRABAJO/_Programación/"

print(listdir(ruta2))

with open("/TRABAJO/_Programación/prueba2.txt", "w") as f:

    f.write('prueba')
    f.close()
"""

"""directorio = "/Users/noave/Downloads"
listArchivos = listdir(directorio)
for fichero in listArchivos:
    if mimetypes.guess_type(fichero)[0] == "image/jpeg":
        print(fichero)"""

"""for fichero in listArchivos:
    if path.isfile(path.join(directorio, fichero)):
        print(fichero)"""

leido='directorio = "/Users/noave/Downloads"'
patron=re.compile(r'"(\S+)"')

print(re.findall(patron, leido))