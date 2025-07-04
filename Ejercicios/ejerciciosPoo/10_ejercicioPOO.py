# 10.Gestión de Biblioteca. Escribe un programa de consola que simula la gestión de una
#  biblioteca. Cada libro debe tener un título, un autor y un estado (prestado o
#  disponible). Crea una clase Libro con los atributos mencionados y métodos para
# prestar y devolver libros. Implementa una clase Biblioteca que almacena una lista de
#  libros y permite buscar libros por título o autor, así como mostrar el estado de un
#  libro específico.

class Libro:
    def __init__(self,titulo,autor,estado):
        self.titulo=titulo
        self.autor=autor
        self.estado=estado

    def prestar_libro(self):
        self.estado="Prestado"
    
    def devolver_libro(self):
        self.estado="Disponible"


class Biblioteca():


    libros = [
        Libro( "Cien años de soledad","Gabriel García Márquez","Disponible"),
        Libro("1984","George Orwell","Prestado"),
        Libro("El principito","Antoine de Saint-Exupéry","Disponible"),
        Libro("Fahrenheit 451","Ray Bradbury","Disponible"),
        Libro("Don Quijote de la Mancha","Miguel de Cervantes","Prestado"),
    ]


    def mostrar_libros(self):
        for libro in self.libros:
            print(f"libro:{libro.titulo}")
            print(f"autor:{libro.autor}")
            print(f"estado:{libro.estado}")



    def agregar_libro(self):
        
        titulo_libro=input("ingrese el nombre de el libro: ")
        autor_libro=input("ingrese el nombre del autor de el libro: ")
        
        self.libros.append(Libro(titulo_libro,autor_libro,"Disponible"))
        
            
    def eliminar_libro(self):
        pass

    
    def buscar_libro(self,titulo,autor,libros):
        libro=None
        for libro in libros:
            if libro["titulo"] == titulo:
                print(libro)
            if libro["autor"] == autor:
                print(libro)
        self.mostrar_estado(libro)

    def mostrar_estado(libro):
        print(libro["estado"])

    def cambiar_estado(self):
        pass
        


class Menu:
    biblioteca=Biblioteca()
    def __init__(self):
        self.menu_opciones={
            "1":self.biblioteca.mostrar_libros,
            "2":self.biblioteca.agregar_libro,
            "3":self.biblioteca.eliminar_libro,
            "4":self.biblioteca.buscar_libro,
            "5":self.biblioteca.mostrar_estado,
            "6":self.salir,
        }

    def mostrar_menu(self):
        print("1- Mostrar libros")
        print("2- Agregar Libro")
        print("3- Eliminar Libro")        
        print("4- Buscar Libro")
        print("5- Mostrar estado")
        print("6- Salir ")

        
        while True:
            try:
                opcion=input("Ingresar opcion: ")
            except ValueError:
                print("valor erroneo: ")

            accion= self.menu_opciones.get(opcion)
            
            if accion: 
                accion()
            else:
                print("opcion invalida")
      

    def salir():
            exit()
