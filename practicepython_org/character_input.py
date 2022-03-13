import datetime

hoy = datetime.date.today()
anioactual = hoy.year

#anioactual = int(hoy.strftime('%Y'))

def centenario(n):
    global anioactual
    cumple = anioactual - n + 100
    print("Cumplirás 100 años en ", cumple)


nombre = input("Introduce tu nombre: ")
print("Tu nombre es " + nombre)
edad = int(input("Introduce tu edad: "))
print("Tu edad es ", edad)


centenario(edad)
