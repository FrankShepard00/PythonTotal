"""
Generadores y decorador. 

1. Perfumería 
2. Farmacia 
3. Cosmeticos
"""

def decorador_turno(funcion): 
    
    def funcion_decorada(turno):
        print("Su turno es: ")
        funcion(turno)
        print("Aguarde y será atendido \n")
    
    return funcion_decorada


def generador_turnos(seccion):
    numero = 1
    while True:
        yield f"     {seccion[0].upper()}-{numero}"
        numero += 1
