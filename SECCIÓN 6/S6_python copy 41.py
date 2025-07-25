'''
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
'''
def registro_error(archivo):
    contenido = open(archivo, "a", encoding='utf-8')
    contenido.write("se ha registrado un error de ejecución")
    contenido.close()
    