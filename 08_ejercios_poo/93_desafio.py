# crea un programa que sea capaz de solicitar un numero y 
# se encargue de imprimir su tabla de multiplicar entre el 1 y el 10

def multiplicacion(num):
    for numero in range(1,11):
        print(f"{numero} x {num} = {num*numero}")


multiplicacion(3)
multiplicacion(6)