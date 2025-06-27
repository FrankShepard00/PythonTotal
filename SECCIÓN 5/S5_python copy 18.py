def cantidad_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            suma = suma + numero
        else:
            pass
    
    return suma

lista_numeros = [1, 2, 3, 4, 5, 4000, 1000, 999, 4]
resultado = cantidad_pares(lista_numeros)
print(resultado)
