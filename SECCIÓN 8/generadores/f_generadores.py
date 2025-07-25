def gen_vidas():
    
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te queda 1 vida"
    yield "Game Over"
    
perder_vida = gen_vidas()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
