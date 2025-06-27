def cantidad_pares(lista_numeros):
    contador = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            contador += 1
    return contador

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
resultado = cantidad_pares(lista_numeros)
print(resultado)


