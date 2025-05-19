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


    if len(expresiones) % 2 != 0:
        return f"Expresion no balanceada: {expresiones}"

    return expresiones


def despejar(expresiones):
    
    for expresion in expresiones:
        if expresion not in ["[","]","(",")","{","}"]:
            expresiones=expresiones.replace(expresion,"")

    return expresiones

print(expresion_equilibrada( "[ a * ( c + d ) ] - 5 }"))










