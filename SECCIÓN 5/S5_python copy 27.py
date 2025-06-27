numeros = [5, 10, 15, 20, -2, 4]

for num in numeros:
    if num < 0:
        print("Error: número negativo encontrado")
        break
    print(f"Procesando: {num}")
else:
    print("Todos los números son validos") # Solo si se procesaron todos
    