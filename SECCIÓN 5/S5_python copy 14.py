def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100, 1000):
            return True 
        else:
            pass
        
    return False
        
resultado = chequear_3_cifras([6000, 1999, 6000])
print(type(resultado))
print(resultado)