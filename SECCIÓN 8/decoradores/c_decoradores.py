
def cambiar_letras(tipo):
    
    def mayuscula(texto):
        print(texto.upper())
    
    def minusculas(texto):
        print(texto.lower())
        
    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minusculas
    
operacion = cambiar_letras('may')

operacion('palabra')
