with open('SECCIÓN 6/CarpetaArchivos/S6_python copy 5/texto.txt', 'w+', encoding='utf-8') as mi_archivo:
    mi_archivo.write(
'''Soy el nuevo texto 
y ahora soy un texto 
de varias líneas''')
    mi_archivo.seek(0)
    print(mi_archivo.read())
    
"""
Soy el nuevo texto 
y ahora soy un texto
de varias líneas
"""