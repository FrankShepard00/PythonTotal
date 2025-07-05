mi_archivo = open("C:\Mis apps\Python TOTAL\SECCIÓN 6\CarpetaArchivos\S6_python\prueba.txt", "r")
todas = mi_archivo.readlines()
print(todas)
mi_archivo.close()
todas = todas.pop()
print(todas)
mi_archivo.close()


'''
['Esta es la primera linea\n', 'Esta es la segunda linea\n', 'Esta es la tercera linea\n', 'Esta es la cuarta linea']
Esta es la cuarta linea
'''