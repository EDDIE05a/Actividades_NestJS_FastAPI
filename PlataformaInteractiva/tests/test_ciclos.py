import unittest
from temas import ciclos

class TestCiclos(unittest.TestCase):
    def test_correcta(self):
        self.assertTrue(ciclos.ejercicio_1("3"))

    def test_incorrecta(self):
        self.assertFalse(ciclos.ejercicio_1("dos"))

if __name__ == "__main__":
    unittest.main()
