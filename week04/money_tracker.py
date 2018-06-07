from aggregated_money_tracker import AggregatedMoneyTraker
from category import Income, Expense


class MoneyTracker:
    def __init__(self, aggregatedMT):
        if type(aggregatedMT) is not AggregatedMoneyTraker:
            raise TypeError
        self.aggregated = aggregatedMT

    def show_user_data(self):
        return "\n".join(self.aggregated.data)

    def show_user_data_for_specific_date(self, date):
        result = []
        for item in self.aggregated.incomes:
            if item.date == date:
                result.append(str(item))
        for item in self.aggregated.expenses:
            if item.date == date:
                result.append(str(item))
        return "\n".join(result)

    def show_user_expenses_ordered_by_categories(self):
        return "\n".join(
            [str(item) for item in sorted(self.aggregated.expenses)])

    def list_incomes(self):
        return "\n".join([str(item) for item in self.aggregated.incomes])

    def list_expenses(self):
        return "\n".join([str(item) for item in self.aggregated.expenses])

    def add_income(self, amount, name, date):
        self.aggregated.add_income(Income(amount, name, date))

    def add_expense(self, amount, name, date):
        self.aggregated.add_expense(Expense(amount, name, date))

    def save(self):
        self.aggregated.save_file()


def main():
    pass
