def decorar_saludo(funcion):
    
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios\n')
        
    return otra_funcion

def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())
    
minuscula_decorada = decorar_saludo(mayusculas)

minuscula_decorada('Minuscula')
minusculas('Minuscula')
