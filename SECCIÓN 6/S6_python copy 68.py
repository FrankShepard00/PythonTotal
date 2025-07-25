class Animal: 
    pass

class Pajaro(Animal):
    pass

print(Pajaro.__bases__)
# Salida: (<class '__main__.Animal'>,)
print(Animal.__subclasses__())
# (<class '__main__.Animal'>,)
# [<class '__main__.Pajaro'>]
