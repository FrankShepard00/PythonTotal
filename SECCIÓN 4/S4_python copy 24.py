dic = {
    'clave1':'a', 
    'clave2':'b', 
    'clave3':'c'
}

for values in dic.values():
    print(values)
# a
# b
# c

for item in dic.items():
    print(item)
# ('clave1', 'a')
# ('clave2', 'b')
# ('clave3', 'c')

for claves,valores in dic.items():
    print(claves +":"+ valores)
    
# clave1:a
# clave2:b
# clave3:c
