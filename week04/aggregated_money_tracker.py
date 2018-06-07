from category import Income, Expense
from parse_money_tracker_data import Parser


class AggregatedMoneyTraker:
    def __init__(self, parser):
        self.parser = parser
        self.data = self.parser.file
        self.incomes = []
        self.expenses = []

    def generate_categories_from_parser(self):
        for item in self.data:
            if '===' in item:
                date = item.split('===')[1].replace(' ', '')
            else:
                temp = item.split(', ')
                if temp[2] == 'New Income':
                    if '.' in temp[0]:
                        income = Income(float(temp[0]), temp[1], date)
                    else:
                        income = Income(int(temp[0]), temp[1], date)
                    self.incomes.append(income)
                else:
                    if '.' in temp[0]:
                        expense = Expense(float(temp[0]), temp[1], date)
                    else:
                        expense = Expense(int(temp[0]), temp[1], date)
                    self.expenses.append(expense)

    def add_income(self, income):
        self.incomes.append(income)
        if f'=== {income.date} ===' in self.data:
            indx = self.data.index(f'=== {income.date} ===')
            self.data.insert(indx + 1, str(self.incomes[-1]))

    def add_expense(self, expense):
        self.expenses.append(expense)
        if f'=== {expense.date} ===' in self.data:
            indx = self.data.index(f'=== {expense.date} ===')
            self.data.insert(indx + 1, str(self.expenses[-1]))

    def save_file(self):
        self.parser.save_file()


def main():
    par = Parser("money_tracker.txt")
    par.make_rows()

    agg = AggregatedMoneyTraker()
    agg.generate_categories_from_parser(par)

    print([str(income) for income in agg.incomes])
    print([str(income) for income in agg.expenses])


if __name__ == '__main__':
    main()
