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
    
    
piolin = Pajaro("amarillo", "canario")
print("Piolin es de color "+piolin.color)
piolin.pintar_negro()
print("Piolin es de color "+piolin.color)
