import unittest
from parse_money_tracker_data import Parser
from aggregated_money_tracker import AggregatedMoneyTraker
from category import Income, Expense


class AggregatedMoneyTrakerTests(unittest.TestCase):
    def setUp(self):
        self.par = Parser("money_tracker.txt")
        self.par.make_rows()
        self.agg = AggregatedMoneyTraker(self.par)
        self.agg.generate_categories_from_parser()

    def test_aggregated_incomes(self):
        expected = ['760, Salary, New Income', '50, Savings, New Income',
                    '200, Deposit, New Income']
        actual = [str(income) for income in self.agg.incomes]
        self.assertEqual(actual, expected)

    def test_aggregated_expenses(self):
        expected = ['5.5, Eating Out, New Expense',
                    '34, Clothes, New Expense', '41.79, Food, New Expense',
                    '12, Eating Out, New Expense', '7, House, New Expense',
                    '14, Pets, New Expense', '112.4, Bills, New Expense',
                    '21.5, Transport, New Expense', '15, Food, New Expense',
                    '5, Sports, New Expense']
        actual = [str(income) for income in self.agg.expenses]
        self.assertEqual(actual, expected)

    def test_add_income(self):
        expected = ['760, Salary, New Income',
                    '50, Savings, New Income',
                    '200, Deposit, New Income',
                    '350, Savings, New Income']
        self.agg.add_income(Income(350, 'Savings', '22-03-2018'))
        actual = [str(income) for income in self.agg.incomes]
        self.assertEqual(actual, expected)

    def test_add_expense(self):
        expected = ['5.5, Eating Out, New Expense',
                    '34, Clothes, New Expense', '41.79, Food, New Expense',
                    '12, Eating Out, New Expense', '7, House, New Expense',
                    '14, Pets, New Expense', '112.4, Bills, New Expense',
                    '21.5, Transport, New Expense', '15, Food, New Expense',
                    '5, Sports, New Expense', '50, Food, New Expense']
        self.agg.add_expense(Expense(50, 'Food', '22-03-2018'))
        actual = [str(income) for income in self.agg.expenses]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
