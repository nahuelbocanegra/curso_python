import re 

#[ coinciden con un conjunto de caracteres dentro de los corchetes

texto="rub.$ius69+"
pattern=r"^[\w._%+-]+$"

match=re.search(pattern,texto)

if match:print("el usuario es valido",match.group())
else:print("no es valido")


#buscar caracteres
texto="hola mundo"

pattern=r"[aeiou]"

match=re.findall(pattern,texto)

print(match)

#una regex que encuentra las malabras man , fan ,ban pero ignora las otras

texto = "man ran fan ñan ban omniman"
pattern=r"^[mfn]an"

match=re.findall(pattern,texto)

print(match)


#[^] coincide con cualquier caracter que no esye dentro de los corchetes 

text="hola mundo"
pattern=r"[^aeiou]"

match=re.findall(pattern,text)
print(match)

