
def nombre_de_la_funcion():
    #docstring
    #cuerpo de la funcion
    print("hola")


nombre_de_la_funcion()


def funcion1 (nombre):
    print(f"hola {nombre}")

funcion1("nahuel")

# argumento es lo que le pasa a la funcion
# parametro es lo que acepta la funcion 

def sum(a,b):
    return a + b

print(sum(4,5))

#documentar la funcion , se hace dentro de la funcion

def resta(a,b):
    """resta dos numeros y devuelve el resultado"""
    return a - b

print(resta.__doc__)
print(help(resta))


def multiplicar(a,b=2):
    return a*b


print(multiplicar(2))


#argumentos por clave
#los parametros son posicionales
def describir_persona(nombre,edad):
    print(f"soy {nombre} y tengo {edad}")

describir_persona(25,"nahuel")
describir_persona("nahuel",10)

#argumento por clave
#parametros nombrados

describir_persona(edad=26,nombre="nahuel")

#argumentos de longitud de variable(*arg)

def numeros(*args):
    for i in args:
        print(i)

numeros(1,2,3,4,5,6,7,8)

#argumentos de clave:valor variables (**kwargs)


def datos(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}:{valor}")


datos(nombre="nahuel",edad=25)