import unittest
from generators import chain, compress


class GeneratorsTests(unittest.TestCase):

    def test_chain(self):
        expected = [0, 1, 2, 3, 4, 5, 6, 7]
        actual = list(chain(range(0, 4), range(4, 8)))
        self.assertEqual(actual, expected)

    def test_compress(self):
        expected = ["Panda"]
        actual = list(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
