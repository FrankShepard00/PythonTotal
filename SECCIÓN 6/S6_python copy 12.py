registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# Abrimos en modo 'a' para agregar sin borrar el contenido existente
with open("registro.txt", "a") as archivo:
    archivo.writelines("\t".join(registro_ultima_sesion) + "\t\n")

# Volvemos a abrir en modo lectura para imprimir el contenido completo
with open("registro.txt", "r") as archivo:
    print(archivo.read())
