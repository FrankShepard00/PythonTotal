from random import choice

def lanzar_moneda():
    return choice(["Cara", "Cruz"])


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]

def probar_suerte(moneda, lista_numeros):
    
    if moneda == "Cara":
        print("La lista se autodestruirá")
        lista_numeros.clear()
    else:
        print("La lista fue salvada")
        
    return lista_numeros
    

probar_suerte(lanzar_moneda(), lista_numeros)
print(lista_numeros)
