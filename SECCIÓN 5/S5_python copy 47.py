
def esDobleCero(*args):
   
    contador = 0 
    
    for num in args:    
        if contador + 1 == len(args):
            return False    
        if args[contador] == 0 and args[contador + 1] == 0:
            resultado = True
            return resultado
        else:
            contador += 1
        
    return resultado
    


listado = [5,6,1,0,9,3,5,0,0]
print(esDobleCero(*listado))