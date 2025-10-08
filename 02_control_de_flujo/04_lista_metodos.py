lista=[1,2,3,4,5,6]

#añadir una elemento al final de la lista

lista.append(10)

#insertar un elemento en una posicion 

lista.insert(1,11)  #(indice,elemento)


# añadir varios elementos al final de lista
lista.extend([22,23]) 

#eliminar elemento de la lista

lista.remove(1) #elimina el primer elemento que encuentra

#elimanar el ultimo elemento por defecto y tambien por indice

lista.pop() #(indice)

#eliminar lista

del lista


#eliminar todo los elementos de la lista

lista.clear()

#eliminar un rango de elementos

lista1 =[1,2,3,4,5,6]
del lista[1:3]


#ordenar listas 

num=[3,6,7,4,2,1,9]

num.sort()#modifica la lista

print(num)

#ordenando lustas creando una nueva
numeros=[8,4,3,6,2,7,1]
sorted_numeros=sorted(numeros)
print(sorted_numeros)

print("ordenar una listas de cadenas de texto")
letras=["a","d","f","l","p","v"]
sorted_letras=sorted(letras)

print("ordenar una listas de cadenas de texto")
letras=["A","a","B","f","F","p","v"]
letras.sort(key=str.lower)
print(letras)
#contar cuantas veces aparece un elemento en la lista
print(letras.count("a"))
