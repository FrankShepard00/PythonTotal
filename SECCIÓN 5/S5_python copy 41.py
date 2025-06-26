def cantidad_atributos(*args, **kwargs):
    return len(args) + len(kwargs)

print(cantidad_atributos(1, 2, nombre="Carlos", edad=30))  # 2 args + 2 kwargs = 4
