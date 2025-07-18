import os

try:
    os.makedirs('C:\\Mis apps\\Python TOTAL\\Archivos\\otra')
    print("El archivo ha sido creado")
except FileExistsError:
    print("El archivo ya existe")
    