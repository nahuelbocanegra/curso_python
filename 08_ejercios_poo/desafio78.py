#  Crea un programa que detecte cuando el famoso "Código Konami" se ha
#  introducido correctamente desde el teclado.
#  Si sucede esto, debe notificarse mostrando un mensaje en la terminal.


def detectar_konami():

    codigo_konami_lista = ["up", "up", "down", "down", "left", "right", "left", "right", "b", "a"]
    entrada=[]

    print("Ingrese las direcciones/exit para salir: ")

    while True:


        codigo=input("> ")

        if codigo.lower() == "exit":
            print("chau")
            break

        entrada.append(codigo)

        if codigo_konami_lista == entrada:
            
            print("codigo kinami correcto: ")

            break
        

detectar_konami()