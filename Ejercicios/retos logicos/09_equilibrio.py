#   Crea un programa que comprueba si los paréntesis, llaves y corchetes
#   de una expresión están equilibrados.
#   - Equilibrado significa que estos delimitadores se abren y cieran
#     en orden y de forma correcta.
#   - Paréntesis, llaves y corchetes son igual de prioritarios.
#     No hay uno más importante que otro.
#   - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#   - Expresión no balanceada: { a * ( c + d ) ] - 5 }


def expresion_equilibrada(expresiones):    

    expresiones=despejar(expresiones)
    expresion_copia=expresiones


    if len(expresiones) % 2 != 0:
        return f"Expresion no balanceada: {expresiones}"


    for i in range(3):
        expresiones=expresiones.replace("()","")
        expresiones=expresiones.replace("[]","")
        expresiones=expresiones.replace("{}","")
       
    if len(expresiones) == 0:
        return f"Expresion balanceada: {expresion_copia}"

    return f"Expresion no balanceada: {expresion_copia}"

def despejar(expresiones):
    
    return ''.join([c for c in expresiones if c in "[](){}"])

print(expresion_equilibrada( "{[ a * ( c + d ) ] - 5 }"))









