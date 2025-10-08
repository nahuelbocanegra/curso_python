persona={
    "nombre":"nahuel",
    "edad":25,
    "dato":33
}

#acceder a los valores

print(persona["nombre"])

#modificar datos
persona["nombre"]="Juan"
print(persona["nombre"])

#elimina datos
del persona["nombre"]
print(persona)

edad=persona.pop("edad") #elimina y recuperarlo el valor
print(edad)


#update

#sobreescribir un dic con otro dic
a={"a":"a"}
b={"a":"z","b":"b" , "c":"c"}

a.update(b)
print(a)

print("a" in a)
print("z" in a)


#obtenes keys
print(persona.keys())
#obtener valores
print(persona.values())
# keys:values
print(persona.items())


lista=[1,2,3,4,5]
goal=6

def dicci():
    dic={}
    for index,num in enumerate(lista):
        falta=goal-num  
        if falta in  dic: return [dic[falta],index]

        dic[num]=index
    return None
 

print(dicci())