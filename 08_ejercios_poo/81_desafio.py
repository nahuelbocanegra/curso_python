#   Crea una función que reciba una expresión matemática (String)
#   y compruebe si es correcta. Retornará true o false.
#   - Para que una expresión matemática sea correcta debe poseer
#     un número, una operación y otro número separados por espacios.
#     Tantos números y operaciones como queramos.
#   - Números positivos, negativos, enteros o decimales.
#   - Operaciones soportadas: + - * / %
#  
#   Ejemplos:
#   "5 + 6 / 7 - 4" -> true
#   "5 a 6" -> false

def encontrar_expresion_pmatematica(expresion):

    expresion=expresion.replace(" ","")

    print(expresion)
    for i in expresion:
        if i in  ["+","-","*","/"] or i.isnumeric():

            continue
        
        return False
        

    return True

print(encontrar_expresion_pmatematica("5 + 6 / 7 x 4"))
