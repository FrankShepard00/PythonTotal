import os
ruta = os.chdir('C:\\Mis apps\\Python TOTAL\\Archivos')
archivo = open('Archivo1.txt', 'r', encoding='utf-8')
print(archivo.read())