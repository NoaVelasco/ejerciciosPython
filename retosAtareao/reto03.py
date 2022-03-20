# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco

# Para el proyecto "reto-python" 
# de Lorenzo Carbonell <a.k.a. atareao>

import mimetypes
from os import listdir, path
import re

def main():
    
    rutaDiogenes = path.join(path.expanduser(
        "~"), '.config\diogenes\diogenes.conf')

    if path.isfile(rutaDiogenes):
        with open(rutaDiogenes, "r") as f:
            print(f.read())

    else:
        with open(rutaDiogenes, "w") as f:
            f.write('directorio = "/Users/noave/Downloads"')
            

    with open(rutaDiogenes, "r") as f:
        dwnldDir = f.readline()

    reemplazo1 = re.sub(r"""[ ="]""", "", dwnldDir)
    reemplazo2 = re.sub(r"""directorio""", "", reemplazo1) 

    listArchivos = listdir(reemplazo2)
    for fichero in listArchivos:
        if mimetypes.guess_type(fichero)[0] == "image/jpeg":
            print(fichero)
        
 

if __name__ == "__main__":
    main()



