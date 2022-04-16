# Python 3.10.2 UTF-8

import random


def guess(x):
    """Se pide al usuario que acierte el número aleatorio. Con pistas."""
    random_number = random.randint(1, x)
    guess_n = 0
    intentos = 0
    # Hasta que no acierte:
    while int(guess_n) != random_number:
        guess_n = int(input(f'Adivina un número entre 1 y {x}: '))
        intentos += 1
        # pistas:
        if guess_n < random_number:
            print(f"¡Uy! No. Más alto que {guess_n}")
        elif guess_n > random_number:
            print(f"No. ¡Vaya! Más bajo que {guess_n}")
    print('¡Acertaste!')
    # Número de intentos:
    if intentos > 1:
        print(f"Has necesitado {intentos} intentos.")
    else:
        print("¡Enhorabuena! ¡Has acertado a la primera!")


def comp_guess(x):
    """Se supone que ahora adivina la máquina."""
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':  # mientras la respuesta no sea correcta.
        # va a generar números hasta que se nivelen low y high
        if low != high:
            guess_n = random.randint(low, high)
        else:
            guess_n = low  # o high, porque son lo mismo
        # hay que darle pistas o decirle si ha acertado:
        feedback = input(
            f'¿{guess_n} es muy alto (A), muy bajo (B) o correcto (C)??\n'.lower())
        # Si es muy alto, baja el tope
        if feedback == 'a':
            high = guess_n - 1
        # Si es muy bajo, sube el mínimo
        elif feedback == 'b':
            low = guess_n + 1

    print(f'¡Bien! He acertado el número {guess_n}. 🥳')


comp_guess(100)
