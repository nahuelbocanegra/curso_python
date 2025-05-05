import re

# Meta caracteres
#los metacaracteres son simbolos especiales con significado especifico en las expresiones regullares
###


#el punto (.) 
#coincidir con cualquier caracter excepto una nueva linea

text="hola mundo,h0la de nuevo ,h=la otra vez"
pattern="h.la"

found = re.findall(pattern,text)

if found:
    print(found)
else: 
    print(" no se ha econtrado el patron ")

text = "casa caasa cosa cisa cesa causa"
pattern= "c.sa" #el punto solo representa a un caracter

matches= re.findall(pattern,text)
print(matches)


#-------------------

text="hola mundo,h0la de nuevo ,h=la otra vez"
pattern=r"h.la" 

found = re.findall(pattern,text)

if found:
    print(found)
else: 
    print(" no se ha econtrado el patron ")

text = "casa caasa cosa cisa cesa causa"
pattern= "c.sa" #el punto solo representa a un caracter

matches= re.findall(pattern,text)
print(matches)

#-------------------

#como usar la barra invertida para anular el significado especial de un simbolo

text="mi casa es blanca. y el coche es negro."
pattern=r"\."
matches=re.findall(pattern,text)

print(matches)


# \d coincide con cualquier digito (0-9)

text="el numero de telefono es 123456789"
found=re.findall(r"\d{9}",text)
print(found)


#detectar si hay un numero en de españa

text="mi numero de telefono es +34 688999999"
pattern=r"\+34 \d{9}"
found = re.search(pattern,text)

if found: print(f"encontre el numero de telefono {found.group()}")

#\w coincide con cualquier caracter alfanumerico (a_z,A_Z,0_9....)
text="@@el rubius_69"
pattern=r"\w"
found=re.findall(pattern,text)
print(found)

#espacio en blanco (tabulacion,salto de linea, espacio)

text="Hola mundo\n¿como estas?\t"
pattern=r"\s"
matches= re.findall(pattern,text)
print(matches)

# ^ = coincide con el principio de una cadena 
text ="@432_name"
pattern=r"^\w" #validar nombre de usuario

valid= re.search(pattern,text)

if valid:
    print("el nombre de usuario es valido") 
else: print("el nombre de usuario no es valido")

phone="+34 49994994"
pattern = r"^\+\d{1,3} "

valid=re.search(pattern,phone)

if valid: print("el telefono no es valido")
else:print("el numero de telefono no es valido")

# $ coincidir con el final de una cadena

text= "hola mundo"
pattern = r"mundo$"

valid = re.search(pattern,text)

if valid : print("la cadena es valida")
else: print("la cadena no es valida")

#validar que in correo se gmail

text="manu@gmail.com"
pattern=r"@gmail.com$"

valid= re.search(pattern,text)

if valid : print("el correo es valida")
else: print("el correo no es valida")

#ejercicio 
#teneo una lista de archivos, necesitamos los nombres de los fichros con extension .txt

files="file1.txt file2.pdf mi.webp texto.txt"


#\b coincide cpn el prinipio o final de una palabra

text= "casa casada casado"
pattern=r"\bcasa\b"

found=re.findall(pattern,text)

print(found)

# | coincidir con una opcion u otra

fruits = "platano, manzana , aguacate , palta ,pera"
pattern = r"palta|aguacate|p..a@|\b\w{7}\b"

matches=re.findall(pattern,fruits)
print(matches)