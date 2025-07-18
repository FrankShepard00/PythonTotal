import os

try:
    ruta = 'C:\\Mis apps\\Python TOTAL\\Archivos\\otra'
    os.rmdir(ruta)
    print("La carpeta ha sido eliminada")
except FileNotFoundError:
    print("La carpeta ya no existe")

