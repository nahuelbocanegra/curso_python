#  4. Cuenta Bancaria. Crea una clase CuentaBancaria con los siguientes atributos
#  obligatorios: número de cuenta, nombre y apellido. El saldo debe comenzar con
#  100.000. Agrega e implementa métodos para: 1- depositar (debe aceptar un valor
#  entero y sumarlo al saldo), 2- retirar (debe aceptar un valor entero y restarlo al saldo
#  sólo si hay dinero suficiente para retirar en la cuenta) y 3- ver saldo. Además, escribe
#  una aplicación de consola que permita al usuario depositar, retirar o ver saldo hasta
#  que decida detenerse. Al finalizar deberá mostrar los datos de la cuenta y el saldo.


class CuentaBancaria:

    def __init__(self,numero_cuenta,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        self.numero_cuenta=numero_cuenta
        self.saldo=100000
    
    def depositar(self,ingreso):
            
        if not isinstance(ingreso,int):
            return "debe ser un entero"
        if ingreso <= 0:
            return "debe ser mayor a 0"
        
        self.saldo+=ingreso
        return f"Ingreso exitoso {ingreso},Nuevo saldo {self.saldo}"

    def retirar(self,retirar):

        if not isinstance(retirar,int):
            return "debe ser un entero"
        if retirar <= 0:
            return "debe ser mayor a 0"
        if self.saldo <= 0:
            return "saldo insuficiente"
        if self.saldo>=retirar:
            self.saldo-=retirar
            return f"retiro de {retirar} exitoso,Nuevo saldo {self.saldo}"
        else:
            return "Saldo Insuficiente"
    
    def ver_saldo(self):
        return f" tu saldo es de {self.saldo} "
    
def main():

    while True:

        print("1- Crear cuenta")
        print("2- Depositar ")
        print("3- Retirar ")
        print("4- Ver Saldo ")
        print("5- Salir ")

        try:
            opcion=int(input("Ingresar una opcion: "))
        except ValueError:
            print("entrada invalida")
            continue

        if opcion == 1:

            try:

                nombre=input("Ingrese su nombre: ")
                apellido=input("Ingrese su apellido: ")
                numero_cuenta=int(input("Ingrese el numero de cuenta: "))

                cuenta=CuentaBancaria(nombre,apellido,numero_cuenta)
                print("cuentra creada exitosamente")
            except ValueError:
                print("dato invalido")




        if opcion == 2:
            deposito=int(input("Ingresar deposito: "))
            cuenta.depositar(deposito)

        if opcion == 3:
            retiro=int(input("ingresa retiro: "))
            cuenta.retirar(retiro)

        if opcion == 4:
            cuenta.ver_saldo()

        if opcion == 5:
            break


if __name__ == "__main__":
    main()