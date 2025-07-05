archivo = open('mi_archivo.txt', 'w+')
archivo.write("Nuevo texto")
archivo.seek(0)
print(archivo.read())