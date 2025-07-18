def generador_funcion():
    numero = 1
    while True: 
        yield numero 
        numero += 1

generador = generador_funcion()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))