class Bill:
    def __init__(self, amount):
        if type(amount) is not int:
            raise TypeError
        if amount < 0:
            raise ValueError
        self.amount = amount

    def __str__(self):
        return 'A {0}$ bill'.format(self.amount)

    def __repr__(self):
        return 'A {0}$ bill'.format(self.amount)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)
