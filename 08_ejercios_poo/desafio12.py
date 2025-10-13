#   Crea una función que reciba dos cadenas como parámetro (str1, str2)
#   e imprima otras dos cadenas como salida (out1, out2).
#   - out1 contendrá todos los caracteres presentes en la str1 pero NO
#     estén presentes en str2.
#   - out2 contendrá todos los caracteres presentes en la str2 pero NO
#      estén presentes en str1.


def generar_cadenas(str1,str2):

    for caracter in str1:

        if caracter in str2:

            str1=str1.replace(caracter,"")
            str2=str2.replace(caracter,"")


    return [str1,str2] 

generar_cadenas("solas","olass")
   
