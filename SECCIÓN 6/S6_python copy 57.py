class Pajaro: 
    alas = True
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        
    def piar(self):
        print('Pio, mi color es {}'.format(self.color))
        
    def volar(self, metros):
        print("El {} ha volado {} metros".format(self.especie, metros))
        
piolin = Pajaro('amarillo', 'canario')

piolin.piar()
piolin.volar(50)       
