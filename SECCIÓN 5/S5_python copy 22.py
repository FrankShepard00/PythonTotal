from random import shuffle

# Lista inicial 
palitos = ['-', '--', '---', '----']

# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# Pedirle intento 

def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un número del 1 al 4:  ")
        
    return int(intento)

intento1 = probar_suerte()
print(intento1)

# Comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("Perdiste")
    else:
        print("Ganaste")
        
    print(f"Te ha tocado {lista[intento-1]}")
    
palitos_mezcaldos = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezcaldos, seleccion)
    
    
    
    