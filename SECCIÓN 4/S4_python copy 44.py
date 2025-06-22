lista = ['a', 'b', 'c']                             # Lista de elementos
pares_indice_valor = list(enumerate(lista))        # Convierte enumerate en una lista de tuplas (índice, valor)

print(type(pares_indice_valor))                    # Muestra el tipo: <class 'list'>
print(pares_indice_valor)                          # Muestra: [(0, 'a'), (1, 'b'), (2, 'c')]
print(pares_indice_valor[1][0])                    # Muestra el índice del segundo elemento: 1

