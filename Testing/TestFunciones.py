# Se importa esta libreria la cual nos permite hacer pruebas unitarias de funciones
# Unittest es un módulo integrado de Python para escribir y ejecutar pruebas automáticas
import unittest 
from Funciones import sumar, mayorQue


# Se crea una clase para testear las funciones
# La clase TestSuma hereda los metodos de la clase TestCase. La clase TestCase usa los metodos de unittest para aplicar las pruebas

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        # assertEqual permite verificar si a y b son iguales
        self.assertEqual(sumar(2, 3), 5)

    def test_mayorQue_true(self):
        # assertTrue permite verificar si la condicion es verdadera
        self.assertTrue(mayorQue(5, 4))

    def test_mayorQue_false(self):
        # assertFalse permite verificar si la condicion es falsa
        self.assertFalse(mayorQue(2, 8))

# Este bloque permite ejecutar el test directamente
if __name__ == '__main__':
    unittest.main()



    