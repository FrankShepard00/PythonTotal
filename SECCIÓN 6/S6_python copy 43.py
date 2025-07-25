from pathlib import Path

ruta = Path('C:\Mis apps\Python TOTAL\SECCIÓN 6') 
carpeta = ruta.parents[0]
print(carpeta) # C:\Mis apps\Python TOTAL
carpeta = ruta.parents[1]
print(carpeta) # C:\Mis apps


'''
Los elementos serían:

ruta.parents[0]: C:/Users/Usuario/Desktop/Curso Python/Cuestionario Día 6

ruta.parents[1]: C:/Users/Usuario/Desktop/Curso Python

ruta.parents[2]: C:/Users/Usuario/Desktop

ruta.parents[3]: C:/Users/Usuario
'''

# Salida: C:/Users/Usuario
