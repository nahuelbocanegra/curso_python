#condicionales
import os
os.system("clear")

print("sentencia simples condicionales")

edad= int(input("que edad tienes: "))

if edad >=18:
    print("eres mayor de edad")
else:
    print("eres menor")

nota=7

# OPERADORES

#or
#and
#!

if nota < 5:
    print("desaprobado") 
elif nota <= 7 and nota >=5:
    print("aprobado")
elif nota >= 7 and nota >= 8:
    print("exelente")


#MALA PRACTICA - CONDICIONALES ANIDADOS

if edad >= 4:
    if edad >5:
        print(edad)





