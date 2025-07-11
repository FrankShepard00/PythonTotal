''' 

Práctica Zip 3
Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

uno / um / one

dos / dois / two

tres / três / three

cuatro / quatro / four

cinco / cinco / five

El resultado deberá seguir la estructura:

[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]
'''



esp = ["uno", "dos", "tres", "cuatro", "cinco"]
port = ["um", "dois", "três", "quatro", "cinco"]
ing = ["one", "two", "three", "four", "five"]

numeros = list(zip(esp, port, ing))

for esp, port, ing in numeros:
    print(f"El número \"{esp}\", en portugués se dice \"{port}\" y en inglés se dice \"{ing}\".")