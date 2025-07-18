"""
Perfumería 
Farmacia 
Cosmeticos

A cual de las areas quiere dirigirse. 

¿Otro turno? 

Su turno es: 
C-5
Aguarde y será atendido 

"""

from numeros import decorador_turno, generador_turnos
import os 

def limpiar_consola():
    os.system('cls')

@decorador_turno
def mostrar_turno(turno):
    print(turno)

def iniciar_turnos():
    limpiar_consola()
    perfumeria = generador_turnos("Perfumeria")
    farmacia = generador_turnos("Farmacia")
    cosmeticos = generador_turnos("Cosmeticos")
    
    while True:
        try:
            print("Bien venido al programa de turnos")
            print("1. Perfumería")
            print("2. Farmacia")
            print("3. Cosméticos")
            print("4. Salir")
            opcion = int(input("Ingresa la opción deseada: "))
            match opcion:
                case 1:
                    limpiar_consola()
                    mostrar_turno(next(perfumeria))
                    
                case 2: 
                    limpiar_consola()
                    mostrar_turno(next(farmacia))
                    
                case 3: 
                    limpiar_consola()
                    mostrar_turno(next(cosmeticos))
                case 4:
                    limpiar_consola()
                    print("Usted ha salido del programa")
                    break
                    
                case _:
                    limpiar_consola()
                    print("Opción no valida")
        except ValueError:
            limpiar_consola()
            print("Esa no es una opción válida")
        
                
        
            
iniciar_turnos()
    

