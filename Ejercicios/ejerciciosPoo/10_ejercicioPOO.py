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
        {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "estado": "Disponible"},
        {"titulo": "1984", "autor": "George Orwell", "estado": "Prestado"},
        {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "estado": "Disponible"},
        {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "estado": "Disponible"},
        {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "estado": "Prestado"},
    ]
    def mostrar_libros():
        pass
    def agregar_libro():
        pass
    def eliminar_libro():
        pass
    def mostrar_estado():
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
        



