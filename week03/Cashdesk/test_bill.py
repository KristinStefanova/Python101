import unittest
from bill import Bill


class BillTest(unittest.TestCase):
    def setUp(self):
        self.a = Bill(10)
        self.b = Bill(5)
        self.c = Bill(10)

    def test_bill_amount_type(self):
        with self.assertRaises(TypeError):
            Bill("15")

    def test_bill_for_negative_amount(self):
        with self.assertRaises(ValueError):
            Bill(-15)

    def test_bill_dunder_int(self):
        self.assertEqual(int(self.a), 10)

    def test_bill_dunder_str(self):
        self.assertEqual(str(self.a), "A 10$ bill")

    def test_bill_dunder_repr(self):
        self.assertEqual(repr(self.a), "A 10$ bill")

    def test_bill_dunder_eq(self):
        self.assertFalse(self.a == self.b)
        self.assertTrue(self.a == self.c)

    def test_bill_dunder_hash(self):
        money_holder = {}
        money_holder[self.a] = 1
        self.assertEqual(money_holder[self.a], 1)


if __name__ == '__main__':
    unittest.main()
