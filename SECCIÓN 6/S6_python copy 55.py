class Cubo: 
    caras = 6
    def __init__(self, color):
        self.color = color
        
        
cubo_rojo = Cubo("rojo")     
print(f"Mi cubo tiene {cubo_rojo.caras} caras y es de color {cubo_rojo.color}.")
