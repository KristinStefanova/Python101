from bill import Bill
from batch_bill import BatchBill

class CashDesk:
    def __init__(self):
        self.desk = []

    def take_money(self, money):
        if type(money) is BatchBill:
            self.desk.extend(money)
        elif type(money) is Bill:
            self.desk.append(money)
        else:
            raise TypeError

    def total(self):
        return sum([int(bill) for bill in self.desk])

    def inspect(self):
        result = {str(bill) + 's': self.desk.count(bill) for bill in self.desk}
        for bill, count in result.items():
            print(bill + " -", count)


def main():
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total())
    desk.inspect()


if __name__ == '__main__':
    main()
