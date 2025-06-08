'''
El programa pide el nombre del usuario 
pide adivinar un numero entre el 1 y el 100 
y tiene 8 intentos para adivinar
Dependiendo de la respuesta el programa puede decir 4 cosas distintas
    a) Si el númeor esta fuera del rango (1 - 100) le va a decir que elija un número permitido
    b) Si el número es mayor al que ha elegido el programa tiene que pedir uno mas bajo. 
    c) Si el número es menor tiene que pedir uno mas alto. 
    d) Si el usuario acierta el programa tiene que decirle que ha ganado y le tiene que decir los intentos que le llevó. 
Si el usuario no ha acertado en los 8 intentos se le pedírá que elija otro numero, así hasta que gane o el usuario decida dejar de jugar. 
'''
from random import randint

print("####___Adivina el número___###")
print("¡Tienes 8 intentos!")
quiere_jugar = 'y'
nombre_usuario = input("¿Cuál es tu nombre? ")

while quiere_jugar.lower() == 'y':
    print("Inicia el juego")
    numero_adivinar = randint(1, 100)
    print(f"¡Genial {nombre_usuario}!")
    intentos = 0

    while intentos < 8:
        try:
            numero_usuario = int(input(f"Llevas {intentos} intentos, ¿en qué número estoy pensando? "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if numero_usuario < 1 or numero_usuario > 100:
            print("Estás fuera de rango (1-100)")
        elif numero_usuario < numero_adivinar:
            print("Elige un número más grande")
        elif numero_usuario > numero_adivinar:
            print("Elige un número más pequeño")
        else:
            print(f"¡Felicidades {nombre_usuario}, ganaste!")
            print(f"Has adivinado en {intentos + 1} intentos")
            break

        intentos += 1

    if intentos >= 8:
        print(f"Te has quedado sin intentos. El número era {numero_adivinar}.")

    quiere_jugar = input(f"¿Quieres jugar de nuevo {nombre_usuario}? y/n ")
    if quiere_jugar.lower() != 'y':
        print(f"Juego terminado, ¡gracias por jugar {nombre_usuario}!")

