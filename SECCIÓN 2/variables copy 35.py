'''
Programa: Calculadora de comisiones 
    1. Preguntar nombre y ventas que han generado
    2. El programa contestará con una frase que contenga: nombre y monto.
        - Ejemplo: "Ok Juan, este mes ganaste $650
    3. Asegurate de que el valor de la  venta transformarlo a float, con 2 decimales
    4. Necesitamos calcular el 13% de la cantidad ingresada (venta * 13 / 100) 
'''
print("Calcula tus comisiones")
print("Por favor ingresa los datos solicitados: ")
nombre = input("Ingresa tu nombre: ")
ventas = float(input("Ingresa tus ventas: "))
comision = round((ventas * 13) / 100, 2)
print(f"Ok {nombre}, este mes ganaste {comision} pesos")
