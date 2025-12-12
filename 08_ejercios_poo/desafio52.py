#  Crea una función que sea capaz de encriptar y desencriptar texto
#  utilizando el algoritmo de encriptación de Karaca
#  (debes buscar información sobre él).


def encriptar_karaca(text):


    text=text[::-1]

    text=text.replace("a",str(0))
    text=text.replace("e",str(1))
    text=text.replace("i",str(2))
    text=text.replace("o",str(3))
    text=text.replace("u",str(4))
    
    
    return text+"aca"
        




encriptar_karaca("hola")