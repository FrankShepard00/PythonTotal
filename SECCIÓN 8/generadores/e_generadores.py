def funcion_gen():
    num = 1
    while True:
        yield num * 7
        num += 1
        
    
generador = funcion_gen()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))