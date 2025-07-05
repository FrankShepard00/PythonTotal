def lista_atributos(**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(valor)        
    return lista


print(lista_atributos(a = 1, b = 2, c = 3))




