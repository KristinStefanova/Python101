import unittest
from parse_money_tracker_data import Parser


class ParserTests(unittest.TestCase):
    def setUp(self):
        self.one = Parser("money_tracker.txt")

    def test_make_rows(self):
        expected = ['=== 22-03-2018 ===', '760, Salary, New Income',
                    '5.5, Eating Out, New Expense', '34, Clothes, New Expense',
                    '41.79, Food, New Expense', '12, Eating Out, New Expense',
                    '7, House, New Expense', '14, Pets, New Expense',
                    '112.4, Bills, New Expense',
                    '21.5, Transport, New Expense',
                    '=== 23-03-2018 ===', '50, Savings, New Income',
                    '15, Food, New Expense',
                    '200, Deposit, New Income', '5, Sports, New Expense']
        self.one.make_rows()
        actual = self.one.file
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
