
e = open("Anki\Hola.txt", "a")
e.write("\nTexto agregado")

e = open("Anki\Hola.txt", "r", encoding='UTF-8')

for x in e:
    print(x)
    
e.close()




