precios_cafe = [
    ('capuchino', 1.5), 
    ('Expresso', 2.2), 
    ('moca', 1.9)
]

for cafe, precio in precios_cafe:
    print(cafe, precio)
    
def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''
    
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
    
    return (cafe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")