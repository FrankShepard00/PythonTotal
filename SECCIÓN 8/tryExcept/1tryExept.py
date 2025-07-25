def suma():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    
    print(n1 + n2)
    print("Gracias por sumar")
    
try:
    # Código que queremos probar
    suma()
except: 
    # Código que se ejecuta si falla
    print("Algo no ha salido bien")
else:
    # Código que se ejecuta si no hay error
    print("Hiciste todo bien")
finally: 
    # Código que se  va a ejecutar de todos modos. 
    print("Eso fue todo")
    