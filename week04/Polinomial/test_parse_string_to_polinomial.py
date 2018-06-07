import unittest
from parse_string_to_polinomial import Parser


class ParserTests(unittest.TestCase):
    def setUp(self):
        f_x1 = "2*x^2+2*x+1"
        f_x2 = "2*x^3+x"
        f_x3 = "1"
        f_x4 = "x^4+10*x^3"
        f_x5 = "1+x^2"
        f_x6 = "3*x^2"
        f_x7 = "6*x"
        self.parser1 = Parser(f_x1)
        self.parser2 = Parser(f_x2)
        self.parser3 = Parser(f_x3)
        self.parser4 = Parser(f_x4)
        self.parser5 = Parser(f_x5)
        self.parser6 = Parser(f_x6)
        self.parser7 = Parser(f_x7)

    def test_init_parser_dict(self):
        with self.assertRaises(TypeError):
            Parser({})

    def test_init_parser_tuple(self):
        with self.assertRaises(TypeError):
            Parser(())

    def test_init_make_list1(self):
        expected = ["2*x^2", "2*x", "1"]
        actual = self.parser1.polinomial_list
        self.assertEqual(actual, expected)

    def test_init_make_list2(self):
        expected = ["2*x^3", "x"]
        actual = self.parser2.polinomial_list
        self.assertEqual(actual, expected)

    def test_init_make_list3(self):
        expected = ["1"]
        actual = self.parser3.polinomial_list
        self.assertEqual(actual, expected)

    def test_init_make_list4(self):
        expected = ["x^4", "10*x^3"]
        actual = self.parser4.polinomial_list
        self.assertEqual(actual, expected)

    def test_init_make_list5(self):
        expected = ["1", "x^2"]
        actual = self.parser5.polinomial_list
        self.assertEqual(actual, expected)

    def test_init_make_list6(self):
        expected = ["3*x^2"]
        actual = self.parser6.polinomial_list
        self.assertEqual(actual, expected)

    def test_init_make_list7(self):
        expected = ["6*x"]
        actual = self.parser7.polinomial_list
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
