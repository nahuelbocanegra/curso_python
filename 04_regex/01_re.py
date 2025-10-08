#expresion regulares
#son una secuencia de caracteres  que forman un patron de busqueda 


""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

# 1ro importar el modulo re

import re

# 2 crear un patron, que queremos encontrar

pattern="hola"

text="hola mundo"

result=re.search(pattern,text)

print(result)

if result:
    print("lo encontre")
else:
    print("no lo encontre")

    
#METODOS re

#group devuelve la cadena que coincide con el patron
print(result.group())
#.start() devolver la posicion inicial de la coincidencia
#end() devolver la posicion donde termina
print(result.start())
print(result.end())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"

result=re.search(pattern,text)


if result :
    print(result.start())
    print(result.end())
else:
    print("no se encontro el patron del texto")

#----------------------

#encontrar toda las coincidencia de un patron .pindall()

text= "me gusta python. python es lo maximo. aunque python no es tan dificil, ojo con python."
pattern= "python"

matches=re.findall(pattern,text) #retorna un lista con toda las coincidencias 

print(len(matches))


#------------------------------------------------------------------------

#iter() devuelve un iterador que contienetoda los resultados de la busqueda

text= "me gusta python. python es lo maximo. aunque python no es tan dificil, ojo con python."
pattern= "py.hon" # . el punto es un caractr especial puede ser cualquier letra 

matches = re.finditer(pattern,text) #devuelve tod las coincidencias con su indice inicial y final

for match in matches:
    print(match.group(),match.start(),match.end())




