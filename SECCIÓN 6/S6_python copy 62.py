# Métodos de clase

class Pajaro: 
    alas = True
    
    def __init__(self, color, especie): #Método constructor
        self.color = color
        self.especie = especie
        
    def piar(self): # metodo de instancia afectan a self osea alas atributos
        print("pio")
        
    def volar(self, metros):
        print(f"el pájaro vuela {metros} metros")
        self.piar()
        
    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pájaro es {self.color}")
        
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
    
    
Pajaro.poner_huevos(3) # Los métodos de clase se pueden llamar sin objetos
# no pueden acceder a los atributos de instancia. 


