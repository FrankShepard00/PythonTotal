from pathlib import Path

# Creamos una ruta ficticia a un archivo
ruta = Path("C:/Users/Usuario/Documents/informe_final.pdf")

# Obtenemos solo el nombre del archivo sin la extensión
nombre_sin_extension = ruta.stem

print(nombre_sin_extension)
#Salida: informe_final

