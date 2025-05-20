#  9-Anagrama. Escribe una función que reciba dos palabras y retorne
#  verdadero o falso según sean o no anagramas.
#  ● Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
#  otra palabra inicial.
#  ● NO hace falta comprobar que ambas palabras existen.
#  ● Dos palabras exactamente iguales no son anagrama

def anagrama (str1,str2):

    if str1 == str2:
        return False
    
    str1="".join(sorted(str1))
    str2="".join(sorted(str1))

    if str1 == str2:
        return True
    
    return False