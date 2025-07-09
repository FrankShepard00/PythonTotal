import os

try:
    ruta = 'C:\\Mis apps\\Python TOTAL\\Archivos\\otra'
    os.rmdir(ruta)
except FileNotFoundError:
    print("La carpeta ya no existe")

