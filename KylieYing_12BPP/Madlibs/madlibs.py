# Python 3.10.2 UTF-8
import random


def madlib1():
    person1PluMas = input("Personajes (masc.): ")
    lugar1 = input("Lugar: ")
    mat1 = input("Material: ")
    return f"A grandes rasgos, la única habilidad que los {person1PluMas} \
de {lugar1} habían descubierto hasta el momento era la capacidad \
de convertir {mat1} en menos {mat1}."


def madlib2():
    nom1PlFem = input("Personajes (fem.): ")
    verb1 = input("Verbo: ")

    return f"A los dioses no les gusta que las {nom1PlFem} no trabajen mucho. \
Las {nom1PlFem} que no están ocupadas continuamente pueden empezar a {verb1}."


def madlib3():
    verb2 = input("Verbo: ")
    obj3SnMas = input("Objeto (masc.): ")

    return f"A veces es mejor {verb2} un {obj3SnMas} que maldecir a la oscuridad."


def madlib4():
    nom2SnFem = input("Sustantivo (fem., sing.): ")
    verb3 = input("Verbo: ")

    return f"Algún día, la {nom2SnFem} aprenderá a {verb3}."


def madlib6():
    verb4 = input("Verbo: ")
    nom3SnMas = input("Sustantivo (masc., sing.): ")
    person1SnMas = input("Personaje (masc., sing.): ")

    return f"Ankh-Morpork había coqueteado con muchas formas de {verb4}, \
y había terminado asumiendo ese tipo de democracia que se conoce como \
‘Un {nom3SnMas}, Un Voto’. El {person1SnMas} era el {nom3SnMas}, y el Voto era el suyo."


def madlib9():
    verb5 = input("Verbo: ")
    nom4SnMas = input("Sustantivo (masc., sing.): ")
    adj1PlMas = input("Adjetivo (masc., pl.): ")
    obj4SnFem = input("Objeto (fem.): ")

    return f"Conozco a las personas que hablan de {verb5} por el bien común. \
¡Nunca son ellos, joder! Cuando oyes a un {nom4SnMas} gritar: ¡Adelante, \
{adj1PlMas} camaradas!, verás que siempre es el que está detrás de la \
jodida {obj4SnFem} enorme, y el único que lleva el casco realmente \
a prueba de flechas."


aleatorio = random.randint(0, 5)

if aleatorio == 0:
    print(madlib1())
elif aleatorio == 1:
    print(madlib2())
elif aleatorio == 2:
    print(madlib3())
elif aleatorio == 3:
    print(madlib4())
elif aleatorio == 4:
    print(madlib6())
elif aleatorio == 5:
    print(madlib9())
