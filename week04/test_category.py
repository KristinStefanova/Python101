import unittest
from category import Category, Income, Expense


class CategoryTests(unittest.TestCase):
    def setUp(self):
        self.one = Category(35, "Food")
        self.two = Category(620, "Salary")
        self.three = Category(35, "Food")

    def test_type_init_category(self):
        with self.assertRaises(TypeError):
            Category([], "")
            Category(12, {})

    def test_amount_init_category(self):
        with self.assertRaises(ValueError):
            Category(-15, "")

    def test_str_category(self):
        self.assertEqual(str(self.one), "35, Food")

    def test_eq_categories_false(self):
        self.assertFalse(self.one == self.two)

    def test_eq_categories_true(self):
        self.assertTrue(self.one == self.three)


class IncomeTests(unittest.TestCase):
    def setUp(self):
        self.one = Income(620, "Salary", '22-03-18')
        self.two = Income(120, "Savings", '22-03-18')

    def test_type_init_income(self):
        with self.assertRaises(TypeError):
            Income([], "", '22-03-18')
            Income(12, {}, '22-03-18')

    def test_amount_init_income(self):
        with self.assertRaises(ValueError):
            Income(-15, "", '22-03-18')

    def test_str_income(self):
        self.assertEqual(str(self.one), "620, Salary, New Income")


class ExpenseTests(unittest.TestCase):
    def setUp(self):
        self.one = Expense(35, "Food", '22-03-18')
        self.two = Expense(50, "Eating Out", '22-03-18')

    def test_type_init_income(self):
        with self.assertRaises(TypeError):
            Expense([], "", '22-03-18')
            Expense(12, {}, '22-03-18')

    def test_amount_init_income(self):
        with self.assertRaises(ValueError):
            Expense(-15, "", '22-03-18')

    def test_str_income(self):
        self.assertEqual(str(self.one), "35, Food, New Expense")


if __name__ == '__main__':
    unittest.main()
