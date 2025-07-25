import os

ruta = "C:\Mis apps\Python TOTAL\SECCIÓN 6\Hola"
try:
    os.makedirs(ruta)
    print("Carpetas creadas exitosamente.")
except FileExistsError:
    print("La carpeta ya existe.")