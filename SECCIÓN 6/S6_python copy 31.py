from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
guia2 = guia.with_name("La_pedrera.txt")
print(guia)
print(guia2)

#C:\Users\frank\Europa\España\Barcelona\Sagrada_Familia.txt
#C:\Users\frank\Europa\España\Barcelona\La_pedrera.txt
