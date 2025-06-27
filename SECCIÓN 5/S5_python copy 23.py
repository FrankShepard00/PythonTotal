from random import randint
def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    
    return (dado1, dado2)

    
dadoUno,dadoDos = lanzar_dados()

def evaluar_jugada(dado_uno, dado_dos):
    suma_dados = dado_uno + dado_dos
    if suma_dados <= 6: 
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    
    
print(evaluar_jugada(dadoUno, dadoDos ))
