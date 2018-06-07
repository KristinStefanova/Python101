class Category:
    def __init__(self, amount, name):
        if type(amount) is not float and type(amount) is not int:
            raise TypeError
        if type(name) is not str:
            raise TypeError
        if amount < 0:
            raise ValueError
        self.amount = amount
        self.name = name

    def __str__(self):
        return f'{self.amount}, {self.name}'

    def __eq__(self, other):
        return self.name == other.name and self.amount == other.amount


class Income(Category):
    def __init__(self, amount, name, date):
        if type(amount) is not float and type(amount) is not int:
            raise TypeError
        if type(name) is not str:
            raise TypeError
        if amount < 0:
            raise ValueError
        super().__init__(amount, name)
        self.date = date

    def __str__(self):
        return super().__str__() + ', New Income'

    def get_date(self):
        return self.date


class Expense(Category):
    def __init__(self, amount, name, date):
        if type(amount) is not float and type(amount) is not int:
            raise TypeError
        if type(name) is not str:
            raise TypeError
        if amount < 0:
            raise ValueError
        super().__init__(amount, name)
        self.date = date

    def __str__(self):
        return super().__str__() + ', New Expense'

    def get_date(self):
        return self.date

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()


def main():
    pass


if __name__ == '__main__':
    main()
