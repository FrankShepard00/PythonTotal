def suma_menores(lista):
    suma = 0 
    for numero in lista:
        if numero in range(0, 1000):
            suma = suma + numero
        else:
            pass

    return suma

lista_numeros = [1, 2, 3, 4, 5, 4000, 1000, 999, 4]
resultado = suma_menores(lista_numeros)
print(resultado)
