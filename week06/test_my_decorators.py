import unittest
from my_decorators import accepts, say_hello, deposit, encrypt, get_low


class MyDecoratorsTests(unittest.TestCase):

    def test_accepts(self):
        with self.subTest("test say_hello raise TypeError"):
            with self.assertRaises(TypeError):
                say_hello(4)

        with self.subTest("test deposit raise TypeError"):
            with self.assertRaises(TypeError):
                deposit(4, [])

    def test_encript(self):
        expected = "Igv igv igv nqy"
        self.assertEqual(expected, get_low())


if __name__ == '__main__':
    unittest.main()
