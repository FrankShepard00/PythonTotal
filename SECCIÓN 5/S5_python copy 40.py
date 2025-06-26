def cantidad_atributos(*args, **kwargs):
    total = 0
    for arg in args:
        total += 1
        
    for kwarg in kwargs:
        total += 1
        
    return total


print(cantidad_atributos(1, 2, nombre="Carlos", edad=30))  # 2 args + 2 kwargs = 4
     