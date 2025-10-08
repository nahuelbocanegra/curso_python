# 7- La secuencia de Collatz de un número entero se construye de la siguiente forma:
#  ● si el número es par,se lo divide por dos;
#  ● si es impar,se le multiplica tres y se le suma uno;
#  Lasucesióntermina al llegar a uno.

def secuecia_collatz(num):
    
    print(num,end=" ")


 
    while num != 1:

        if num % 2 == 0:
            num = num // 2 
            
        else :
            num = num * 3 + 1
        
        print(num,end=" ")

        
secuecia_collatz(10)