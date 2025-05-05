import re

#modificadores

#los modificadores son opciones que se pueden agregar a un patron para cambiar su comportamiento 


#re.IGNORECASE

text = "Todo el mundo dice que la iA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado." \
"la ia no estan mala, viva la Ia"
pattern = "IA"

found_ia=re.findall(pattern,text,re.IGNORECASE)

if found_ia:
    print(found_ia)

