from pathlib import Path
carpeta = Path("C:\Mis apps\Python TOTAL\Archivos\Archivo1.txt")

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Este archivo existe")

