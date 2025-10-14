#  Crea un programa que analice texto y obtenga:
#  - Número total de palabras.
#  - Longitud media de las palabras.
#  - Número de oraciones del texto (cada vez que aparecen un punto).
#  - Encuentre la palabra más larga.
# 
#  Todo esto utilizando un único bucle.
 

def analizar_texto(texto):


    texto=texto.replace("," ,"")
    texto=texto.replace("\n"," ")
    texto=texto.split(" ")

    
    datos={
        "longitud_media":0,
        "cantidad_palabras": len(texto),
        "palabra_mas_larga":"",
        "cantidad_oraciones":0
    }

    for palabra in texto:

        if palabra == "":
            continue

        if "." in palabra:
            datos["cantidad_oraciones"]+=1
            palabra=palabra.replace(".","")
        
        if len(datos["palabra_mas_larga"]) < len(palabra):
            
            
            datos["palabra_mas_larga"]=palabra

        datos["longitud_media"]+= len(palabra)

    datos["longitud_media"]= datos["longitud_media"] //len(texto)
    
    return datos


texto="""Python es un lenguaje interpretado, de alto nivel y de propósito general. 
Su filosofía enfatiza la legibilidad del código y una sintaxis que permite a los programadores
expresar conceptos en menos líneas de código."""

print(analizar_texto(texto))