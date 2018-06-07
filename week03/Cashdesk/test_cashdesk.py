import unittest
from bill import Bill
from batch_bill import BatchBill
from cashdesk import CashDesk


class CashdeskTest(unittest.TestCase):
    def setUp(self):
        self.a = Bill(10)
        self.b = Bill(5)
        self.c = Bill(10)
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        self.batch = BatchBill(bills)
        self.desk = CashDesk()
        self.desk.take_money(self.batch)

    def test_desk_total(self):
        self.assertEqual(self.desk.total(), 180)


if __name__ == '__main__':
    unittest.main()
