# 
#   Crea un programa que cuente cuantas veces se repite cada palabra
#   y que muestre el recuento final de todas ellas.
#   - Los signos de puntuación no forman parte de la palabra.
#   - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#   - No se pueden utilizar funciones propias del lenguaje que
#     lo resuelvan automáticamente.
#  


def contando_palabras(texto):
    caracteres=[",",";","-","_","?","¡","¿","?","!","{","}","+","-"]
    palabras={}
    
    for i in texto:
        if i in caracteres:
            texto=texto.replace(i,"")
   
    lista_palabras=texto.split()
    

    for palabra in lista_palabras:
        if palabra in palabras:
            palabras[palabra]+=1
        else:
            palabras[palabra]=1
    
    return palabras
    
print(contando_palabras("hola como estas?"))