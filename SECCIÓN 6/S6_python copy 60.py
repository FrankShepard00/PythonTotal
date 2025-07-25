class Alarma: 
    
    def __init__(self):
        pass
    
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
        
alarma = Alarma()
alarma.postergar(3)
