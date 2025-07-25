# Métodos de clase

class Pajaro: 
    alas = True
    
    def __init__(self, color, especie): #Método constructor
        self.color = color
        self.especie = especie
        
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        print(Pajaro.alas)
    
    
Pajaro.poner_huevos(3)
