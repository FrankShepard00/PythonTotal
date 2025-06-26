def lista_atributos(**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(valor)        
    return lista

dic = {
    'a':'1',
    'b':'2', 
    'c':'3'
}


print(lista_atributos(**dic))