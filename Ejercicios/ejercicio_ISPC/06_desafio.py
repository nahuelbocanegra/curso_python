#  6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un
#  triángulo rectángulo como el de más abajo con tantos renglones como indique el
#  usuario.
def triangulo(renglones):

    cadena=""
    for i in range(renglones):
        cadena+="*"
        print(cadena)


triangulo(18)