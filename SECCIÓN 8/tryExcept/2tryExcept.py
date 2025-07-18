def suma():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    
    print(n1 + n2)
    print("Gracias por sumar")
    
    
try:
    suma()
except TypeError: 
    print("Estas intentado concatenar tipos distintos ")
except ValueError:
    print("Ese no es un número")
finally: 
    print("Programa terminado")