import os

# Ruta completa que queremos crear
ruta = "C:/Users/Usuario/Curso Python/Día 6/Ejercicios"

# Crea todas las carpetas necesarias en la ruta (si no existen)
os.makedirs(ruta, exist_ok=True)

print("Carpetas creadas exitosamente.")
