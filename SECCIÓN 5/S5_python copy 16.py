def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return False
        else:
            pass
    return True

lista_numeros = [2, 3,4,-45,0,54]
resultado = todos_positivos(lista_numeros)
print(resultado)