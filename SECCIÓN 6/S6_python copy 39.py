'''

Práctica Archivos y Funciones 1
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
'''
def abrir_leer(archivo):
    contenido = open(archivo, "r", encoding='UTF-8')
    return contenido.read()