nombre = "Frank"

for letra in nombre: 
    if letra == 'n': 
        break
    else:
        print(letra)
    
print(' ')

for letra in nombre: 
    if letra == 'n': 
        pass
    else:
        print(letra)
        
print('')
        
# Usando continue
for letra in "manzana":
    if letra == 'n':
        continue  # Salta esta iteración
    print(letra)

# Agregar en la explicación la diferencia entre pass y continue
