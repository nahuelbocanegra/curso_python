""" 3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si
 es un número primo o no """


def evaluar_numero():
    divisores=0
    numero=input("Ingrese un numero entero: ")

    while True:
        if numero.isnumeric():
            numero=int(numero)
            break
        else:
            print("Error debe ser un numero entero")
            numero=input("Ingrese un numero entero: ")


    for num in range(2,numero+1):
        if numero % num == 0:
            divisores+=1
        
    if divisores > 2:
        return "No es primo"
    return "Es primo"

print(evaluar_numero())