from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))

print(guia.parent)
print(guia.parent.parent)
print(guia.parent.parent.parent)

