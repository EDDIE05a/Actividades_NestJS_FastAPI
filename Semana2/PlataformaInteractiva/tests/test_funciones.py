import sys
import unittest
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from temas import funciones

class TestFunciones(unittest.TestCase):
    def test_correcta(self):
        self.assertTrue(funciones.ejercicio_1("def"))

    def test_incorrecta(self):
        self.assertFalse(funciones.ejercicio_1("function"))

if __name__ == "__main__":
    unittest.main()
