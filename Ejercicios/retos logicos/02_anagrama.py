# 
#   Escribe una función que reciba dos palabras (String) y retorne
#   verdadero o falso (Bool) según sean o no anagramas.
#   - Un Anagrama consiste en formar una palabra reordenando TODAS
#     las letras de otra palabra inicial.
#   - NO hace falta comprobar que ambas palabras existan.
#   - Dos palabras exactamente iguales no son anagrama.
#  

def anagama(palabra1,palabra2):
    if palabra1 == palabra2:
        return False
    
    palabra1=list(palabra1)
    palabra1="".join(sorted(palabra1))

    palabra2=list(palabra2)
    palabra2="".join(sorted(palabra2))

    if palabra1 == palabra2:
        return True
    return False

print(anagama("hola","ola"))