def suma_absolutos(*args):
    total = 0 
    for arg in args:
        total += abs(arg)
        
    return total

print(suma_absolutos(-2, 3, -4, 5, -6))