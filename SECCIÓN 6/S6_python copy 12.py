registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

with open("registro.txt", "a") as archivo:
    archivo.writelines("\t".join(registro_ultima_sesion) + "\t\n")

with open("registro.txt", "r") as archivo:
    print(archivo.read())
