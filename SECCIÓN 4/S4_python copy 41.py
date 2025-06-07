
import math                     # Importa el módulo math para usar math.pow()
suma_cuadrados = 0              # Inicializa la variable acumuladora

for numero in range(1, 16):     # Recorre los números del 1 al 15 (inclusive)
    suma_cuadrados += math.pow(numero, 2)  # Suma el cuadrado de 'numero'
    print(f"{numero} : {suma_cuadrados}")  # Muestra el número y la suma acumulada
