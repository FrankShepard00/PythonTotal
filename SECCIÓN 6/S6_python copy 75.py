class Padre: 
    
    def hablar(self):
        print("hola")
        
class Madre:
    
    def reir(self):
        print("Jajaja")
        
    def hablar(self):
        print("hablar")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__)