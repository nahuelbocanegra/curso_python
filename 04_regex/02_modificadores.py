import re

#modificadores

#los modificadores son opciones que se pueden agregar a un patron para cambiar su comportamiento 


#re.IGNORECASE

text = "Todo el mundo dice que la iA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado." \
"la ia no estan mala, viva la Ia"
pattern = "IA"

found_ia=re.findall(pattern,text,re.IGNORECASE) #IGNORECASE => no distingue entre may y minuscula

if found_ia:
    print(found_ia) #devuelve toda las condiciones IA


#remplazar el texto


text = "Todo el mundo dice que la iA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado." \
"la ia no estan mala, viva la Ia"

#sub() reemplazar todas las coincidencias de un patron de un texto

text = " hola,mundo ! Hola de nuevo"
pattern = "Hola"
remplacement="Adios"

new_text= re.sub(pattern,remplacement,text)

print(new_text)

