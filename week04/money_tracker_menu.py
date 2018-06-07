from money_tracker import MoneyTracker
from aggregated_money_tracker import AggregatedMoneyTraker
from parse_money_tracker_data import Parser


class MoneyTrackerMenu:
    def __init__(self, name):
        print(f'Hello, {name}!')
        self.option = 0
        self.parser = Parser("money_tracker.txt")
        self.parser.make_rows()
        self.agg = AggregatedMoneyTraker(self.parser)
        self.agg.generate_categories_from_parser()
        self.mt = MoneyTracker(self.agg)

    def start(self):

        while True:
            self.option = int(input("""Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
"""))
            if type(self.option) is not int:
                raise TypeError
            if self.option < 1 or self.option > 6:
                raise ValueError

            if self.option == 1:
                print(self.mt.show_user_data())
            elif self.option == 2:
                date = input("Enter date: ")
                print(self.mt.show_user_data_for_specific_date(date))
            elif self.option == 3:
                print(self.mt.show_user_expenses_ordered_by_categories())
            elif self.option == 4:
                amount = float(input("New income amount: "))
                name = input("New income type: ")
                date = input("New income date: ")
                self.mt.add_income(amount, name, date)
            elif self.option == 5:
                amount = float(input("New expense amount: "))
                name = input("New expense type: ")
                date = input("New expense date: ")
                self.mt.add_expense(amount, name, date)
            if self.option == 6:
                self.mt.save()
                exit()
