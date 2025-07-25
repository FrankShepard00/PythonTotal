'''
Administrador de recetas 

1. Bienvenida al usuario 
    tiene que indicar en donde están las recetas (path)
    y el número de recetas que hay
2. Opciones
    1. Leer receta
    2. Crear Receta
    3. Crear categoría
    4. Eliminar receta]
    5. Eliminar categoría
    6. Finalizar programa
    


'''
from pathlib import Path















def iniciar_programa():
    print("Hola Bienvenido")
    base = Path("C:\Recetas")
    print(f"Todas las recetas de este programa están en la carpeta {base}")
    
    

iniciar_programa()


