'''
Analizador de textos 
1. que el programa pida un texto
2. que ingrese 3 letras 
    - que diga cuantas veces aparecen las letras en el texto(absolutamente todas)
    - Cuantas palabras hay en total 
    - primera letra del texto y la última
    - palabras en orden inverso
    - ¿Aparece python? 
'''

texto = input("Ingresa tu texto: ")
texto = texto.lower()

letras = []
letras.append(input("Ingresa la primera letra para el análisis: ").lower())
letras.append(input("Ingresa la segunda letra para el análisis: ").lower())
letras.append(input("Ingresa la tercera letra para el análisis: ").lower())

total_letra1 = texto.count(letras[0])
total_letra2 = texto.count(letras[1])
total_letra3 = texto.count(letras[2])

print(f"La '{letras[0]}'aparece en el texto {total_letra1} veces")
print(f"La '{letras[1]}' aparece en el texto {total_letra2} veces")
print(f"La '{letras[2]}' aparece en el texto {total_letra3} veces")


total_palabras = texto.split(" ")
print(f"El texto tiene {len(total_palabras)} palabras")


primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"El texto inicia con la letra {primera_letra}")
print(f"El texto termina con la letra {ultima_letra}")

total_palabras.reverse()
texto_invertido = ' '.join(total_palabras)

print(f"El texto al revéz es: {texto_invertido}")
if('python' in texto):
    print("La palabra python si aparece")
else:
    print("La palabra python no aparece")
    