# bucles for
# itera sobre un iterable o una lista

numeros=[1,2,3,4,5,6,7]

for numero in numeros:
    print(numero)

cadena="nahuel"

for letra in cadena:
    print(letra)


#recuperar el indice de cada elemento 
frutas=["mandarina","pera","manzana"]

for index , fruta in enumerate(frutas):
    print(f"{index}:{fruta}")


#bucles anidados

    for numero in numeros:
        print(f"elemento for1 :{numero}")
        for i in numeros:
            print(f"{i}")


#comprension de lista

lista=[numero * 2 for numero in numeros]
print(lista)


pares=[num  for num in [1,2,3,4,5,6] if num % 2 == 0]
print(pares)

