from pathlib import Path, PureWindowsPath
carpeta = Path("C:/Mis apps/Python TOTAL/Archivos/Archivo1.txt")

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)