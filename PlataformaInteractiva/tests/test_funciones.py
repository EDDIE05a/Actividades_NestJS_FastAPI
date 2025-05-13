import unittest
from temas import funciones

class TestFunciones(unittest.TestCase):
    def test_correcta(self):
        self.assertTrue(funciones.ejercicio_1("def"))

    def test_incorrecta(self):
        self.assertFalse(funciones.ejercicio_1("function"))

if __name__ == "__main__":
    unittest.main()
