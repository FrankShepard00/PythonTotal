'''
Práctica Comprensión de Listas 3
Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:

°C = (°F - 32) * (5/9)

o expresado de otro modo:

(grados_fahrenheit-32)*(5/9)

La lista de temperaturas es la siguiente:

temperatura_fahrenheit = [32, 212, 275] 
Almacena esta nueva lista en una variable llamada grados_celsius
'''

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(temperatura -32)*(5/9) for temperatura in temperatura_fahrenheit]

print(grados_celsius)