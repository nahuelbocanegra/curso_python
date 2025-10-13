 #  Crea un programa que realize el cifrado César de un texto y lo imprima.
#  También debe ser capaz de descifrarlo cuando así se lo indiquemos.
# 
#  Te recomiendo que busques información para conocer en profundidad cómo
#   realizar el cifrado. Esto también forma parte del reto.
# 





def cifrado_cesar(texto,desplazamiento):

    alfabeto= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    mensaje=""
    
    for index in texto:
        if index.isalpha():
            nueva_pos=(posicion + desplazamiento) % len(alfabeto)
            posicion = alfabeto.index(index.upper())
            mensaje+=alfabeto[nueva_pos]
            continue
        
        else :
            mensaje+=index
   
    return mensaje
       


print(cifrado_cesar("hola como estas",3))