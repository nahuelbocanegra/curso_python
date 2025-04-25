#listas

lista=[1,2,3,4,5]
lista2=["manzana","perro",2,3]
lista3=[True,False,"manzana","perro",2,3]
lista4=[[1],[2],[3]]

#acesso por indice

print(lista[0])
print(lista2[-1])
print(lista4[1][0])


#slicing

lista_recortada=lista[1:4] #2,3,4 => el indice 4 no lo incorpora 

print(lista[:]) #esta haciendo una copia de la lista
print(lista[::-1]) #devuelve indices inversos
print(lista["desde":"hasta":"paso"])

#añadir elementos a una lista

lista1 = lista + [1,2,3]
lista1 += [10,11,12]

#longuitud de la lista

len(lista1)



