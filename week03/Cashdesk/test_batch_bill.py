import unittest
from bill import Bill
from batch_bill import BatchBill


class BatchBillTest(unittest.TestCase):
    def setUp(self):
        self.a = Bill(10)
        self.b = Bill(5)
        self.c = Bill(10)
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        self.batch = BatchBill(bills)

    def test_batch_bill_type_error(self):
        with self.assertRaises(TypeError):
            BatchBill({})

    def test_batch_bill_value_error(self):
        with self.assertRaises(ValueError):
            BatchBill(['1'])

    def test_batch_bill_total(self):
        self.assertEqual(self.batch.total(), 180)

    def test_batch_bill_len(self):
        self.assertEqual(len(self.batch), 4)


if __name__ == '__main__':
    unittest.main()
