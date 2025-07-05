with open('SECCIÓN 6/CarpetaArchivos/S6_python copy 5/texto.txt', 'a+', encoding='utf-8') as mi_archivo:
    mi_archivo.write('Bienvenido')
    mi_archivo.seek(0)
    print(mi_archivo.read())
    
    
#Hola esto es un archivo Bienvenido