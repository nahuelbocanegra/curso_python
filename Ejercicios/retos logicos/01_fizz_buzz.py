# 
#   Escribe un programa que muestre por consola (con un print) los
#   números de 1 a 100 (ambos incluidos y con un salto de línea entre
#   cada impresión), sustituyendo los siguientes:
#   - Múltiplos de 3 por la palabra "fizz".
#   - Múltiplos de 5 por la palabra "buzz".
#   - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  


def fizzBuzz():
    for num in range(1,101):
        divisiblePorTress=num % 3 == 0
        divisiblePorCinco=num % 5 == 0
        if divisiblePorTress and divisiblePorCinco:
            print("Fizzbuzz")  
        elif divisiblePorTress:
            print("Fizz")   
        elif divisiblePorCinco:
            print("Buzz")
        else:
            print(num)
        
fizzBuzz()