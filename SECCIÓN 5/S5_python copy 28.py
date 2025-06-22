servidores = ["server1", "server2", "server3"]

for servidor in servidores:
    print(f"Intentando conectar a {servidor}")
    if servidor == "server2":
        print("Conexión exitosa")
        break
else:
    print("Limpieza: Ningún servidor disponible")
    print("Activando modo offline")