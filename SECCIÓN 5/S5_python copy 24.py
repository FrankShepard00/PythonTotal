def reducir_lista(lista):
    resultado = []
    for numero in lista:
        if numero not in resultado: 
            resultado.append(numero)
    
    resultado.sort()
    resultado.pop()
    
    
    return resultado

lista_numeros = [1,2,15,7,2]
print(reducir_lista(lista_numeros))



def promedio(lista):
    return sum(lista) / len(lista)
 
    
promedio(lista_numeros)
     
        

            
        
    
    
    



