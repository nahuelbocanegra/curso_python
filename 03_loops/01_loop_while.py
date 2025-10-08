contador=0

while True:
    if contador == 2:
        break #ROMPRE EL BUCLE
    print(contador)
    contador+=1

contador=0


while contador<=10:
    contador+=1
    if contador % 2 == 0:
        continue
    print(contador)




#else
while contador<=10:
    contador+=1
    if contador % 2 == 0:
        #continue
        break
    print(contador)
     
else: #cuando hay un break el else no se cumple por que la condicion nunca va a ser falsa
    print("el bucle a terminado")


numero=-1

while numero < 0: 
    try:
        numero = int(input("Escribir un numero positivo: "))
        if numero < 0:
            print("el numero debe ser positivo:")
    except:
        print("debes ingresar un num: ")
        
print(f"el numero es {numero}")