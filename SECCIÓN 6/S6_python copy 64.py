# Métodos de clase

class Pajaro: 
    alas = True
    
    def __init__(self, color, especie): #Método constructor
        self.color = color
        self.especie = especie
        
        
    @staticmethod
    def mirar():
        print("El pajaro mira")
    #los atributos estáticos no pueden acceder ni a los atributos de la clase 
    #Ni a los atributos de la instancia
        
    
    
Pajaro.mirar()
