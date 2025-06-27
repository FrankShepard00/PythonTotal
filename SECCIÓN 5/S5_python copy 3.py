marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(f"¿Son conjuntos aislados? {conjuntos_aislados}")


elementos_comunes = marcas_smartphones.intersection(marcas_tv)
print(f"Elementos en común: {elementos_comunes}")