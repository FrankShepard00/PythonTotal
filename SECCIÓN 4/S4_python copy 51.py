'''

Práctica Zip 2
Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
'''

marcas = ["Sony", "HP", "Samsung"]
productos = ["Audifonos", "Pantalla", "Celular"]

mi_zip = list(zip(marcas, productos))
print(mi_zip)

for marca, producto in mi_zip:
    print(f"{producto} de la marca {marca}")