
#  *Escribe un programa que se encargue de comprobar si un número es o no primo.
#   Hecho esto, imprime los números primos entre 1 y 100. */
         
    
        
def es_primo(num):

        if num <= 2:
            return False
        
        for i in range(3,num):
            divisible=2
            if num % i == 0:
                divisible+=1

            if divisible >=3:
                return False

        return True

for i in range(1,101):
    if es_primo(i):
        print(f"{i}: es primo")
    else: 
        print(f"{i} no es primo")