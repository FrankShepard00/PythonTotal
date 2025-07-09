







from pathlib import Path

guia = Path(Path.home(),"Downloads", "Europa" )

for txt in Path(guia).glob("*.txt"):
    print(txt)