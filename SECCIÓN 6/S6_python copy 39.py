'''

Práctica Archivos y Funciones 1
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
'''
def abrir_leer(archivo):
    with open(archivo, "r", encoding='UTF-8') as f:
        return f.read()

print(abrir_leer("C:/Mis apps/Python TOTAL/SECCIÓN 6/CarpetaArchivos/S6_python/prueba.txt"))
