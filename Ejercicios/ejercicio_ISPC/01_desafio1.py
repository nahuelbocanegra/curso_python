#  1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el
#  número conlos dígitos en orden inverso

def inverso_numero(num):
    num=str(num)
    num=num[::-1]
    return int(num)
print(inverso_numero(123))