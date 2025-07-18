class Vaca:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self): 
        print("muu")
        
class Oveja:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self): 
        print("bee")
        
vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()
    
# polimorfismo 