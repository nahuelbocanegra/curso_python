#   Crea tres test sobre el reto 12: "Viernes 13".
#   - Puedes copiar una solución ya creada por otro usuario en
#     el lenguaje que estés utilizando.
#   - Debes emplear un mecanismo de ejecución de test que posea
#     el lenguaje de programación que hayas seleccionado.
#   - Los tres test deben de funcionar y comprobar
#     diferentes situaciones (a tu elección).



import unittest
from desafio12 import generar_cadenas

class TestGenerarPalabras(unittest.TestCase):
    def test_generar_palabras(self):
        self.assertEqual(generar_cadenas("hola","sola"),["h","s"])
        self.assertEqual(generar_cadenas("perro","gato"),["perr","gat"])
        self.assertEqual(generar_cadenas("solas","olass"),["",""])




if __name__ == "__main__":
    unittest.main()