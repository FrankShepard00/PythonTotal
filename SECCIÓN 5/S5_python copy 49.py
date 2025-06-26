def contar_primos(rango):
    total = 0 
    for numero in range(2, rango + 1):
        contador = 0
        for divisor in range(1,numero+1, 2):
            #print(numero, "/", divisor, "=", numero/divisor)
            if numero % divisor == 0: 
                #print("entero")
                contador = contador + 1 
        
        if contador == 2:
            print(numero, " es primo")
            total = total + 1
                
        #print("-")        
                
    return total 
                
        
print("El número total de números primos es: ", contar_primos(100))