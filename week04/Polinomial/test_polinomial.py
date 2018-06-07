import unittest
from polinomial import Polinomial, FirstDerivative


class PolinomialTests(unittest.TestCase):
    def setUp(self):
        self.f_x1 = "2*x^2+2*x+1"
        self.f_x2 = "2*x^3+x"
        self.f_x3 = "1"
        self.f_x4 = "x^4+10*x^3"
        self.f_x5 = "1+x^2"
        self.f_x6 = "3*x^2"
        self.f_x7 = "6*x"
        self.f_x8 = "6*x"
        self.polinomial1 = Polinomial(self.f_x1)
        self.polinomial2 = Polinomial(self.f_x2)
        self.polinomial3 = Polinomial(self.f_x3)
        self.polinomial4 = Polinomial(self.f_x4)
        self.polinomial5 = Polinomial(self.f_x5)
        self.polinomial6 = Polinomial(self.f_x6)
        self.polinomial7 = Polinomial(self.f_x7)
        self.polinomial8 = Polinomial(self.f_x8)

    def test_str_f_x1(self):
        expected = f"f(x) = {self.f_x1}"
        actual = str(self.polinomial1)
        self.assertEqual(actual, expected)

    def test_str_f_x2(self):
        expected = f"f(x) = {self.f_x2}"
        actual = str(self.polinomial2)
        self.assertEqual(actual, expected)

    def test_str_f_x3(self):
            expected = f"f(x) = {self.f_x3}"
            actual = str(self.polinomial3)
            self.assertEqual(actual, expected)

    def test_str_f_x4(self):
            expected = f"f(x) = {self.f_x4}"
            actual = str(self.polinomial4)
            self.assertEqual(actual, expected)

    def test_str_f_x5(self):
            expected = f"f(x) = {self.f_x5}"
            actual = str(self.polinomial5)
            self.assertEqual(actual, expected)

    def test_str_f_x6(self):
            expected = f"f(x) = {self.f_x6}"
            actual = str(self.polinomial6)
            self.assertEqual(actual, expected)

    def test_str_f_x7(self):
            expected = f"f(x) = {self.f_x7}"
            actual = str(self.polinomial7)
            self.assertEqual(actual, expected)

    def test_eq_f_x7_f_x8(self):
        self.assertTrue(self.polinomial7 == self.polinomial8)

    def test_eq_f_x7_f_x6(self):
        self.assertFalse(self.polinomial7 == self.polinomial6)


class FirstDerivativeTests(unittest.TestCase):
    def setUp(self):
        self.f_x1 = "2*x^2+2*x+1"
        self.f_x2 = "2*x^3+x"
        self.f_x3 = "1"
        self.f_x4 = "x^4+10*x^3"
        self.f_x5 = "1+x^2"
        self.f_x6 = "3*x^2"
        self.f_x7 = "6*x"
        self.f_x8 = "6*x"
        self.derivative1 = FirstDerivative(self.f_x1)
        self.derivative2 = FirstDerivative(self.f_x2)
        self.derivative3 = FirstDerivative(self.f_x3)
        self.derivative4 = FirstDerivative(self.f_x4)
        self.derivative5 = FirstDerivative(self.f_x5)
        self.derivative6 = FirstDerivative(self.f_x6)
        self.derivative7 = FirstDerivative(self.f_x7)
        self.derivative8 = FirstDerivative(self.f_x8)

    def test_make_derivative_f_x1(self):
        expected = "4*x+2"
        self.derivative1.make_derivative()
        actual = self.derivative1.get_derivative()
        self.assertEqual(actual, expected)

    def test_make_derivative_f_x2(self):
        expected = "6*x^2+1"
        self.derivative2.make_derivative()
        actual = self.derivative2.get_derivative()
        self.assertEqual(actual, expected)

    def test_make_derivative_f_x3(self):
        expected = "0"
        self.derivative3.make_derivative()
        actual = self.derivative3.get_derivative()
        self.assertEqual(actual, expected)

    def test_make_derivative_f_x4(self):
        expected = "4*x^3+30*x^2"
        self.derivative4.make_derivative()
        actual = self.derivative4.get_derivative()
        self.assertEqual(actual, expected)

    def test_derivative_f_x5(self):
        expected = "2*x"
        self.derivative5.make_derivative()
        actual = self.derivative5.get_derivative()
        self.assertEqual(actual, expected)

    def test_make_derivative_f_x6(self):
        expected = "6*x"
        self.derivative6.make_derivative()
        actual = self.derivative6.get_derivative()
        self.assertEqual(actual, expected)

    def test_make_derivative_f_x7(self):
        expected = "6"
        self.derivative7.make_derivative()
        actual = self.derivative7.get_derivative()
        self.assertEqual(actual, expected)

    def test_str_f_x1(self):
        expected = "f'(x) = 4*x+2"
        actual = str(self.derivative1)
        self.assertEqual(actual, expected)

    def test_str_f_x2(self):
        expected = "f'(x) = 6*x^2+1"
        actual = str(self.derivative2)
        self.assertEqual(actual, expected)

    def test_str_f_x3(self):
        expected = "f'(x) = 0"
        actual = str(self.derivative3)
        self.assertEqual(actual, expected)

    def test_str_f_x4(self):
        expected = "f'(x) = 4*x^3+30*x^2"
        actual = str(self.derivative4)
        self.assertEqual(actual, expected)

    def test_false_eq_f_x7_f_x6(self):
        self.assertFalse(self.derivative7 == self.derivative6)

    def test_true_eq_f_x7_f_x8(self):
        self.assertTrue(self.derivative7 == self.derivative8)


def main():
    pass


if __name__ == '__main__':
    unittest.main()
