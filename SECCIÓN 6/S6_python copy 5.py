with open('SECCIÓN 6/CarpetaArchivos/S6_python copy 5/texto.txt', 'w+', encoding='utf-8') as mi_archivo:
    mi_archivo.write('Soy el nuevo texto')
    mi_archivo.write(' y me editaron de nuevo')
    mi_archivo.seek(0)
    print(mi_archivo.read())