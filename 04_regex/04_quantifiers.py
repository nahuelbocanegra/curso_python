import re 

# 03 quantifiers
#los cuantificadores se utilizan para especificar cuantas ocurrencias de 
# un caracteres se deben encontrar en una cadena

# * : puede aparecer 0 o mas veces
text ="aaaba"
pattern="a*"
matches=re.findall(pattern,text)
print(matches)


#cuantas palabras tienen de 0 a mas "a" y despues una b

# + una a mas veces
text="aa bb cc aa dd aa"
pattern="a+"
matches=re.findall(pattern,text)
print(matches)

# ? cero a una vez

text="aaabacb"
pattern="a?b"
matches=re.findall(pattern,text)
print(matches)

#{n} extamente n veces 

text="aaaaaa    aa  aaa  asaa"
pattern=r"a{3}" #devuelve las 3 primeras

matches=re.findall(pattern,text)

print(matches)

#{n , m}: de n a m veces

words="ala casa arbol murcielago leon"
patters=r"\b\w{4,6}\b" #palabras de 2-3 letras
matches=re.findall(patters,words)
print(matches)
