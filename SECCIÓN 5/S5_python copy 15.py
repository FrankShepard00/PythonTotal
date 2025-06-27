def numeros_tres_cifras(lista):
    listaDetres = []
    for n in lista:
        if n in range(100, 1000): 
            listaDetres.append(n)
        else:
            pass
    return listaDetres

lista = [34, 456, 4567, 455, 123, 45]
lista3 = numeros_tres_cifras(lista)
print(lista3)
