def numeros_persona(nombre, *args):
    total = 0 
    for arg in args:
        total += arg
        
    return f"{nombre}, la suma de tus números es {total}"


print(numeros_persona("Frank", 3, 2, 4, -4, 4))   
