'''

Práctica Tipos de Métodos 1
Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
'''

class Mascota:
    def __init__(self):
        pass
    
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
        
Mascota.respirar()
