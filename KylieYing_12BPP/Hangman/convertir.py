with open("lemario.txt", encoding="utf-8") as f:
    palabras = f.read().split('\n')
    
print(len(palabras))
print(palabras[0:12])

with open("palabras.txt", 'w', encoding="utf-8") as f:
    f.write(str(palabras))

# @TODO filtrar palabras y dejar solo las que sean mayores de 5 letras o algo así. 
# Bueno, primero veo el vídeo.
