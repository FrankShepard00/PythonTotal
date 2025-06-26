

# def letras(palabra):
    
    
#     lista = []
#     for letra in palabra:
#         if letra not in lista:
#             lista.append(letra)
#             lista.sort()
        
#     print(lista)
    
    
# letras("entretenido")

def lentras_unicas(palabra):
    mi_set = set()
    
    for letra in palabra:
        mi_set.add(letra)
        
    mi_lista = list(mi_set)
    mi_lista.sort()
    
    return mi_lista

print(lentras_unicas("entretenido"))