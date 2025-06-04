mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a") # 3
print(resultado)

resultado = mi_texto.index("a", 5) # 10
print(resultado)

#resultado = mi_texto.index("a", 5, 10) # ValueError: substring not found
#print(resultado)

resultado = mi_texto.index("a", 5, 11) # ValueError: substring not found
print(resultado)