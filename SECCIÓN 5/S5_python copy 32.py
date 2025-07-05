def suma_cuadrados(*args):
    return sum(arg ** 2 for arg in args)

print(suma_cuadrados(2, 3, 4, 5))