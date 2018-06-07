from bill import Bill


class BatchBill:
    def __init__(self, bills):
        if type(bills) is not list:
            raise TypeError
        if not any([True for bill in bills if type(bill) is Bill]):
            raise ValueError
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum([int(bill) for bill in self.bills])

    def __getitem__(self, index):
        return self.bills[index]
