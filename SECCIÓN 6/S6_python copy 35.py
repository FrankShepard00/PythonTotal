from pathlib import Path

base = Path.home()
guia = Path(base, "Downloads", "Europa", "España", "Barcelona", "Sagrada_Familia.txt")

# Esto sí funciona porque es parte exacta del inicio de 'guia'
en_europa = guia.relative_to(base / "Downloads" / "Europa")
en_espania = guia.relative_to(base / "Downloads" / "Europa" / "España")

print(en_europa)   # España/Barcelona/Sagrada_Familia.txt
print(en_espania)  # Barcelona/Sagrada_Familia.txt
