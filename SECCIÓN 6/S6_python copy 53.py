class Pajaro:
    
    alas = True # En la tercera parte hacer enfasis en atributos de clase
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        
mi_pajaro = Pajaro("negro", "Tucan")

print(f"Mi pajaro es un {mi_pajaro.especie} y su color es de color {mi_pajaro.color}.")
print(Pajaro.alas)
print(mi_pajaro.alas)