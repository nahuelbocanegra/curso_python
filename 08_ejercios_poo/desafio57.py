# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo,
#  * fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */

def es_fibonacci(num):

    fibo=[0,1,1,2]

    for i in range(num):
        fibo.append(fibo[len(fibo)-2]+fibo[len(fibo)-1])

        if num in fibo:

            return True

        if num < fibo[len(fibo)-1]:
            return False
        
def es_par(num):
    if num % 2 == 0:
        return True
    return False

def es_primo(num):

    cantidad=1

    for i in range(2,num):
        print(i)
        if num % i == 0:

            cantidad +=1

        if cantidad >= 2:

            return False
        
    return True
        
    

def comprobar_primo_par_fibonacci(num):


    print(f"primo:{es_primo(num)},fibonacci:{es_fibonacci(num)}, par:{es_par(num)}")

comprobar_primo_par_fibonacci(4)