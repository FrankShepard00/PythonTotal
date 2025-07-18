import os

class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Cliente(Persona):
    
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} \nBalance de cuenta {self.numero_cuenta}: ${self.balance}"
        
    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")

    def retirar(self, monto_retiro):
        if monto_retiro <= self.balance:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")
    
def crear_cliente():
    print("Para crear el usuario, completa los siguientes datos ")
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingresa el apellido: ")
    numero_cuenta = int(input("Ingresa el número de cuenta: "))
    nuevo_cliente = Cliente(nombre, apellido, numero_cuenta)
    return nuevo_cliente
    

def mostrar_opciones():
    return 0

def limpiar_consola():
    os.system('cls')


def inicio():
    print("Hola bienvenido a tu banco")
    cliente = crear_cliente()
    print(cliente)
    
    opcion = 0
    
    while(opcion != 4):
        print("Ingresa la opción deseada")
        print("")
        print("1. Crear nuevo cliente")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        print("")
        
        opcion = int(input("Opción deseada: "))
        match opcion:
            case 1: 
                limpiar_consola()
                print("Crear cliente")
                cliente = crear_cliente()
                limpiar_consola()
                print("¡Cliente creado con éxito!")
                print(cliente)
            case 2:
                limpiar_consola()
                print(cliente)
                deposito = int(input("Ingrese la cantidad a depositar: "))
                cliente.depositar(deposito)
                limpiar_consola()
                print("Depósito realizado.")
                print(cliente)
            case 3: 
                limpiar_consola()
                print(cliente)
                retiro = int(input("Ingrese la cantidad a retirar: "))
                cliente.retirar(retiro)
                limpiar_consola()
                print("Operación completada.")
                print(cliente)
                
            case 4: 
                limpiar_consola()
                print("Ha salido del programa.")
            case _: 
                limpiar_consola()
                print("Opción no válida.")
                
    
inicio()