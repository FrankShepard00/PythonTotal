from pathlib import Path

carpeta = Path("/Mis apps/Python TOTAL/Archivos")
archivo = carpeta / "Archivo1.txt"

mi_archivo = open(archivo, encoding='utf-8')
print(mi_archivo.read())
