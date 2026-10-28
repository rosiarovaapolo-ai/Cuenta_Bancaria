
import json

class Cuenta_Bancaria():
    def __init__(self,titular,saldo):
                 
        self.titular = titular
        self.saldo = saldo
        self.guardar_saldo()

    def guardar_saldo(self):
        datos = {
            "dueño": self.titular,
            "saldo":  self.saldo
        }

        with open("Banco de datos.json", "w") as archivo:
            json.dump(datos, archivo, indent= 4)

    @classmethod
    def cargas_json(cls):
        try:
            with open("Banco de datos.json", "r") as archivo:
                datos = json.load(archivo)
                print("Archivo cargado con exito")
                return cls(datos["nombre"], datos["saldo"])
        except FileNotFoundError:
            print("Archivo no encontrado")
            return None
        
            
        

    def mostrar_saldo(self):
        print(f"Se mostrara su saldo en su cuenta el cual es: {self.saldo}")

    def depositar_saldo(self):
        dep_sal = float(input("Ingrese el saldo que quiera depositar: "))
        if dep_sal > 0:
            self.saldo += dep_sal
            print("Operacion realizada con exito, gracias por usarla")
        else:
            print("Ingrese un saldo mayor a cero")
    
        print(f"Su saldo actual es {self.saldo}")
    def retirar_saldo(self):
        sal_ret = float(input("Ingrese la cantidad que quiera retirar: "))
        if 0 < sal_ret <= self.saldo:
           self.saldo -= sal_ret
           print("Operacion realizada con exito, gracias por usarla")
           
        else:
           print("Fondos insuficientes")
            
        print(f"Su saldo actual es {self.saldo}")

mi_cuenta = Cuenta_Bancaria.cargas_json()

if mi_cuenta is None:
    cuenta_dueño = input("Ingrese su nombre por favor: ").capitalize()
    cuenta_saldo = float(input("Ingrese su saldo por favor: "))
    mi_cuenta = Cuenta_Bancaria(cuenta_dueño, cuenta_saldo)


print("---Menu del Banco---")
print("1. Mostrar Saldo")
print("2. Depositar Saldo")
print("3. Retirar Saldo")
print("4. Salir")

while True:

        opcion = int(input("Ingrese la opcion que quiera ejecutar: "))
        if opcion == 1:
            mi_cuenta.mostrar_saldo()
        elif opcion == 2:
            mi_cuenta.depositar_saldo()     
        elif opcion == 3:
            mi_cuenta.retirar_saldo()
        elif opcion == 4:
            break

        else:
            print("Opcion no valida,escoga otra")


    

