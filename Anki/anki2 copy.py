try:
    f = open("hola.txt", "x", encoding="UTF-8")
    f.write("Hola mundo!")
    print("Archivo creado")
    f.close
except FileExistsError: 
    print("El archivo ya existe: ")
    f = open("hola.txt", "r")
    for x in f: 
        print(x)