import sys
import unittest
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from temas import condicionales

class TestCondicionales(unittest.TestCase):
    def test_correcta(self):
        self.assertTrue(condicionales.ejercicio_1("SI"))

    def test_incorrecta(self):
        self.assertFalse(condicionales.ejercicio_1("NO"))

if __name__ == "__main__":
    unittest.main()
