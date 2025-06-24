#  4. Cuenta Bancaria. Crea una clase CuentaBancaria con los siguientes atributos
#  obligatorios: número de cuenta, nombre y apellido. El saldo debe comenzar con
#  100.000. Agrega e implementa métodos para: 1- depositar (debe aceptar un valor
#  entero y sumarlo al saldo), 2- retirar (debe aceptar un valor entero y restarlo al saldo
#  sólo si hay dinero suficiente para retirar en la cuenta) y 3- ver saldo. Además, escribe
#  una aplicación de consola que permita al usuario depositar, retirar o ver saldo hasta
#  que decida detenerse. Al finalizar deberá mostrar los datos de la cuenta y el saldo.


class CuentaBancaria:
    def __init__(self,numero_cuenta,nombre,apellido):
        self.numero_cuenta=numero_cuenta
        self.nombre=nombre
        self.apellido=apellido
        self.saldo=100000
    
    def depositar(self,ingreso):
        self.saldo+=ingreso

    def retirar(self,retirar):
        if self.saldo <= 0:
            return "saldo insuficiente"
        
        self.saldo-=retirar

        return f"retiro de {retirar} exitoso"
    
    def ver_saldo(self):
        return f" tu saldo es de {self.saldo} "
    
def main():

    while True:

        print("1- Depositar ")
        print("2- Retirar ")
        print("3- Ver Saldo ")
        print("4- Salir ")


        