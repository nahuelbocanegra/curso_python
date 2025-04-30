# 
#   Crea un programa se encargue de transformar un número
#   decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  

def decimal_binario(num):
    binario=""
    while 1 <= num:
        print(num)
        if num % 2 == 0:
            binario+="0"
            num=num//2
        else:
            binario+="1"
            num=num//2
    
    return binario[::-1]
print(decimal_binario(100))


