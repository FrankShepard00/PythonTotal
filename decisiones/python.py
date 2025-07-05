def cantidad_pares(lista_numeros):
    contador = 0
    for numero in lista_numeros:
        if numero % 2 == 0: 
            contador += 1 
        else:
            pass
        
    return contador

print(cantidad_pares([2, 3, 4, 5, 6, 7, 8]))