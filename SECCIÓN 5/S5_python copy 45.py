def devolver_distintos(num1, num2, num3):
    lista = [num1, num2, num3]
    lista.sort()
    suma = sum(lista) 
    print(suma)
    if suma < 10:
        return min(lista)
    elif suma > 15:
        return max(lista)
    else:
        return lista[1] 
    
    
print(devolver_distintos(2, 8, 3))
