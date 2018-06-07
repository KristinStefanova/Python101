import unittest
from parse_money_tracker_data import Parser
from aggregated_money_tracker import AggregatedMoneyTraker
from money_tracker import MoneyTracker


class MoneyTrakerTests(unittest.TestCase):
    def setUp(self):
        self.par = Parser("money_tracker.txt")
        self.par.make_rows()
        self.agg = AggregatedMoneyTraker(self.par)
        self.agg.generate_categories_from_parser()
        self.mt = MoneyTracker(self.agg)

    def test_init_money_tracker(self):
        with self.assertRaises(TypeError):
            MoneyTracker(self.par)

    def test_show_user_data(self):
        expected = "\n".join(['=== 22-03-2018 ===', '760, Salary, New Income',
                              '5.5, Eating Out, New Expense',
                              '34, Clothes, New Expense',
                              '41.79, Food, New Expense',
                              '12, Eating Out, New Expense',
                              '7, House, New Expense', '14, Pets, New Expense',
                              '112.4, Bills, New Expense',
                              '21.5, Transport, New Expense',
                              '=== 23-03-2018 ===', '50, Savings, New Income',
                              '15, Food, New Expense',
                              '200, Deposit, New Income',
                              '5, Sports, New Expense'])
        actual = self.mt.show_user_data()
        self.assertEqual(actual, expected)

    def test_show_user_data_for_specific_date(self):
        date = '22-03-2018'
        expected = "\n".join(['760, Salary, New Income',
                              '5.5, Eating Out, New Expense',
                              '34, Clothes, New Expense',
                              '41.79, Food, New Expense',
                              '12, Eating Out, New Expense',
                              '7, House, New Expense', '14, Pets, New Expense',
                              '112.4, Bills, New Expense',
                              '21.5, Transport, New Expense'])
        actual = self.mt.show_user_data_for_specific_date(date)
        self.assertEqual(actual, expected)

    def test_show_user_expenses_ordered_by_categories(self):
        expected = "\n".join(['112.4, Bills, New Expense',
                              '34, Clothes, New Expense',
                              '5.5, Eating Out, New Expense',
                              '12, Eating Out, New Expense',
                              '41.79, Food, New Expense',
                              '15, Food, New Expense',
                              '7, House, New Expense',
                              '14, Pets, New Expense',
                              '5, Sports, New Expense',
                              '21.5, Transport, New Expense'])
        actual = self.mt.show_user_expenses_ordered_by_categories()
        self.assertEqual(actual, expected)

    def test_list_incomes(self):
        expected = "\n".join(['760, Salary, New Income',
                              '50, Savings, New Income',
                              '200, Deposit, New Income'])
        actual = self.mt.list_incomes()
        self.assertEqual(actual, expected)

    def test_list_expenses(self):
        expected = "\n".join(['5.5, Eating Out, New Expense',
                              '34, Clothes, New Expense',
                              '41.79, Food, New Expense',
                              '12, Eating Out, New Expense',
                              '7, House, New Expense',
                              '14, Pets, New Expense',
                              '112.4, Bills, New Expense',
                              '21.5, Transport, New Expense',
                              '15, Food, New Expense',
                              '5, Sports, New Expense'])
        actual = self.mt.list_expenses()
        self.assertEqual(actual, expected)

    def test_add_income(self):
        expected = ['=== 22-03-2018 ===',
                    '350, Savings, New Income',
                    '760, Salary, New Income',
                    '5.5, Eating Out, New Expense',
                    '34, Clothes, New Expense',
                    '41.79, Food, New Expense',
                    '12, Eating Out, New Expense',
                    '7, House, New Expense',
                    '14, Pets, New Expense',
                    '112.4, Bills, New Expense',
                    '21.5, Transport, New Expense',
                    '=== 23-03-2018 ===',
                    '50, Savings, New Income',
                    '15, Food, New Expense',
                    '200, Deposit, New Income',
                    '5, Sports, New Expense']
        amount = 350
        name = "Savings"
        date = '22-03-2018'
        self.mt.add_income(amount, name, date)
        actual = self.mt.aggregated.data
        self.assertEqual(actual, expected)

    def test_add_expense(self):
        expected = ['=== 22-03-2018 ===',
                    '760, Salary, New Income',
                    '5.5, Eating Out, New Expense',
                    '34, Clothes, New Expense',
                    '41.79, Food, New Expense',
                    '12, Eating Out, New Expense',
                    '7, House, New Expense',
                    '14, Pets, New Expense',
                    '112.4, Bills, New Expense',
                    '21.5, Transport, New Expense',
                    '=== 23-03-2018 ===',
                    '50, Food, New Expense',
                    '50, Savings, New Income',
                    '15, Food, New Expense',
                    '200, Deposit, New Income',
                    '5, Sports, New Expense']
        amount = 50
        name = "Food"
        date = '23-03-2018'
        self.mt.add_expense(amount, name, date)
        actual = self.mt.aggregated.data
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
