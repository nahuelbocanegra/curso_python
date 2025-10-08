#primer reto 1

def alianza(cadena):

    cadena=cadena.lower()
    reed=cadena.count("r")
    jonh=cadena.count("j")

    return reed == jonh

lista="skldajslkfjasdljksadnlnsdalsdnRRR"

print(alianza(lista))


#2do reto

def contador(lista):
  cantidad=0
  for i in lista:
     if i % 2==0:
        cantidad+=i

  return cantidad


print(contador([2,3,4,5,6,7,8,9,10,2,3,4,5]))


#reto 3

num=[4,5,6,2]
goal=8

def encontrar_la_suma(num):
    for i in range(len(num)-1):
         for j in range(i+1,len(num)):
             print(f"{num[i]}:{num[j]}")
             if num[i] + num[j] == goal:
              return[i , j]
    return None

encontrar_la_suma(num)