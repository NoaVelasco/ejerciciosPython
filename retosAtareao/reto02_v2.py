from os import *
import re
import mimetypes

mimetypes.init()

def get_download_folder():
    home = path.expanduser("~")
    return path.join(home, "Downloads")


patronNum = re.compile(r"[0-9]")
dwnldDir = get_download_folder()

print("Directorio: \n", dwnldDir, "\n---------------------------")

contenido = listdir(dwnldDir)
imagenes = []
for fichero in contenido:
    if path.isfile(path.join(dwnldDir, fichero)) and mimetypes.guess_type(fichero)[0] == "image/jpeg":
        imagenes.append(fichero)

pos = 0

for i in imagenes:
    pos += 1
    if pos % 2 == 0:
        i = "==> " + i

    if patronNum.search(i):
        print(i.upper())
    else:
        print(i.lower())
