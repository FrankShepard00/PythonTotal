def mi_funcion():
    return 4

def mi_generador():
    yield 4
    
print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g)) #StopIteration