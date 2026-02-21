import unittest
from main import modulo

class TestModulo(unittest.TestCase):

    def test_modulo_success(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 5), 0)
        self.assertEqual(modulo(7, 4), 3)

    def test_modulo_by_zero(self):
        self.assertRaises(ValueError, modulo, 10, 0)


if __name__ == '__main__':
    unittest.main()

