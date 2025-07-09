import os

try:
    os.makedirs('C:\\Mis apps\\Python TOTAL\\Archivos\\otra')
except FileExistsError:
    print("El archivo ya existe")
    