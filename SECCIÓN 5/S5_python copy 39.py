def prueba(num1, num2, *args, **kwargs):
    print(f"El primer argumento es: {num1}")
    print(f"El segundo argumento es: {num2}")
    
    for arg in args:
        print(f"arg = {arg}")
        
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
 
 
args = [100, 200, 300, 400,]
kwargs = {'x':"uno", 'y':"dos", 'z':"tres"}
 
prueba(15, 50, *args, **kwargs)