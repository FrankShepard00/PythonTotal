'''
Juego del ahorcado 
De una lista de palabras el programa va a elegir una (con el método choise)
El programa va a mostrar una serie de guiones que representarán las letras ocultas _ _ _ _ 
El jugador en cada turno tendrá que elegir una letra y si la letra está en la palabra oculta 
se mostrará en los guiones _ a _ _ a_  en caso de que no sea correcta perderá una vida. 
Si sele terminan las vidas (6) pierde, si adivina antes gana. 
necesitaremos varias funciones como función para pedir letra validar letra, ver si ganó etc. 
'''

from random import choice

def palabraRandom():
    lista_palabras = [
    'caminar', 'espejos', 'ventana', 'palabra', 'montaña', 'respuesta', 'limpieza', 'cultura', 'herencia', 'juguetes',
    'computadora', 'naturaleza', 'verduras', 'colores', 'ciudades', 'encender', 'bosques', 'animales', 'fragancia', 'mensaje',
    'estación', 'persona', 'historia', 'lenguaje', 'pinturas', 'distancia', 'paisajes', 'cosechas', 'teclados', 'numerosa',
    'escritor', 'lector', 'almohada', 'banderas', 'camiseta', 'cuaderno', 'emociones', 'fotografías', 'galletas', 'hambre',
    'ilusión', 'joyería', 'kilómetro', 'liberado', 'memorias', 'noticias', 'olvidado', 'pregunta', 'ratones', 'sabores'
    ]
    
    palabra = list(choice(lista_palabras))
    
    return palabra

def palabraOculta(palabra):
    palabraGuiones = []
    
    for letra in palabra:
        palabraGuiones.append("_")
        
    return palabraGuiones


def comprobar_letra(letra, palabra, guines):
    letra_encontrada = False
     
    contador = 0 
    for letraPalabra in palabra:
        if letraPalabra == letra:
            guines[contador] = letra
            letra_encontrada = True
            
        contador+=1
        
    print("Palabra: ", " ".join(guines))        
    return letra_encontrada
        
def comprobar_si_gano(palabra , guines):
    if palabra == guines:
        return True
    else:
        return False
    
    

def iniciarJuego():
    vidas = 10
    palabra = palabraRandom()
    guines = palabraOculta(palabra)
    print("Juego del ahorcado, tienes 10 vidas")
    haGanado = comprobar_si_gano(palabra, guines)
    alfabeto = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    while vidas > 0 and not haGanado:
        letra = input("Ingresa una letra:  ")
        
        if letra not in alfabeto or len(letra) != 1:  
            print("Ingresa una sola letra válida del alfabeto.")
            continue
            
        intento = comprobar_letra(letra, palabra, guines)
        haGanado = comprobar_si_gano(palabra, guines)
        
        if not intento:
            vidas -= 1
            print(f"Letra incorrecta, tienes {vidas} vidas")
        else:
            print(f"Bien! Letra correcta, tines {vidas} vidas")
    if(haGanado):
        print("Ganaste!")
    else:
        print("Has perdido, la palabra era: " + "".join(palabra))
        
    
    
    
    
iniciarJuego()