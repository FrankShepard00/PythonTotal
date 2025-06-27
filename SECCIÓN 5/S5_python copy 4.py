# Conjunto con marcas de smartphones
marcas_smartphones = {"Xiaomi", "Apple", "Huawei"}

# Conjunto con marcas de televisores
marcas_tv = {"Sony", "Philips", "Panasonic"}

# Se verifica si ambos conjuntos no tienen elementos en común
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

# Se imprime el resultado
print(conjuntos_aislados)  # Resultado: True

