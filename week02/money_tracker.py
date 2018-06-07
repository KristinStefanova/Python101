def list_user_data():
    try:
        f = open('money_tracker.txt')
    except Exception as e:
        print('We hit an error: {}'.format(e))
    else:
        return f.read()
    finally:
        if not f.closed:
            f.close()


def parse_file_by_dates(my_file):
    result = {}
    my_file = my_file.split('\n')
    for line in my_file:
        if '===' == line[0:3]:
            temp_date = line
            result[temp_date] = []
        else:
            temp = line.split(", ")
            if "." in temp[0]:
                result[temp_date].append((float(temp[0]), temp[1], temp[2]))
            else:
                result[temp_date].append((int(temp[0]), temp[1], temp[2]))
    return result


def parse_dict_to_file(d):
    result = ""
    for key, item in d.items():
        result += key + '\n'
        for t in item:
            amount, category, mode = t
            result += str(amount) + ", " + category + ", " + mode + '\n'
    return result[:len(result) - 1]


def show_user_incomes(file):
    result = []
    dict_lines = parse_file_by_dates(file)
    for key in dict_lines.keys():
        for item in dict_lines[key]:
            amount, category, mode = item
            if mode == 'New Income':
                result.append((amount, category))
    return result


def show_user_savings(file):
    result = []
    dict_lines = parse_file_by_dates(file)
    for key in dict_lines.keys():
        for item in dict_lines[key]:
            amount, category, mode = item
            if category == 'Savings':
                result.append((amount, category))
    return result


def show_user_deposits(file):
    result = []
    dict_lines = parse_file_by_dates(file)
    for key in dict_lines.keys():
        for item in dict_lines[key]:
            amount, category, mode = item
            if category == 'Deposit':
                result.append((amount, category))
    return result


def show_user_expenses(file):
    result = []
    dict_lines = parse_file_by_dates(file)
    for key in dict_lines.keys():
        for item in dict_lines[key]:
            amount, category, mode = item
            if mode == 'New Expense':
                result.append((amount, category))
    return result


def list_user_expenses_ordered_by_categories(file):
    result = []
    dict_lines = parse_file_by_dates(file)
    for key in dict_lines.keys():
        for item in dict_lines[key]:
            amount, category, mode = item
            if mode == 'New Expense':
                result.append((amount, category))
    return sorted(result, key=lambda x: x[1])


def show_user_data_per_date(date, file):
    result = []
    dict_lines = parse_file_by_dates(file)
    for key in dict_lines.keys():
        if date in key:
            result = dict_lines[key]
    return result


def list_income_categories(file):
    result = []
    dict_lines = parse_file_by_dates(file)
    for key in dict_lines.keys():
        for item in dict_lines[key]:
            amount, category, mode = item
            if mode == 'New Income' and category not in result:
                result.append(category)
    return result


def list_expense_categories(file):
    result = []
    dict_lines = parse_file_by_dates(file)
    for key in dict_lines.keys():
        for item in dict_lines[key]:
            amount, category, mode = item
            if mode == 'New Expense' and category not in result:
                result.append(category)
    return result


def add_income(income_category, money, date, file):
    if type(income_category) is not str:
        raise TypeError
    if type(date) is not str:
        raise TypeError
    if type(money) is not (int or float):
        raise TypeError
        dict_lines = parse_file_by_dates(file)
        key = "=== " + date + " ==="
        if key in dict_lines.keys():
            dict_lines[key].append((money, income_category, "New Income"))
        else:
            dict_lines[key] = [(money, income_category, "New Income")]
        f = open('money_tracker.txt', 'w')
        result = parse_dict_to_file(dict_lines)
        f.write(result)
        f.close()


def add_expense(expense_category, money, date, file):
    if type(expense_category) is not str:
        raise TypeError
    if type(date) is not str:
        raise TypeError
    if type(money) is not (int or float):
        raise TypeError
        dict_lines = parse_file_by_dates(file)
        key = "=== " + date + " ==="
        if key in dict_lines.keys():
            dict_lines[key].append((money, expense_category, "New Expense"))
        else:
            dict_lines[key] = [(money, expense_category, "New Expense")]
        f = open('money_tracker.txt', 'w')
        result = parse_dict_to_file(dict_lines)
        f.write(result)
        f.close()


def main():
    name = input("What is your name? ")
    print("Hello, ", name, "!\n")

    flag = True
    while flag:
        try:
            choice = int(input("""Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
"""))
        except ValueError:
            print("Invalid number")
        else:
            file = list_user_data()
            if choice == 1:
                print(file)
            elif choice == 2:
                date = input("Enter date")
                print(show_user_data_per_date(date, file))
            elif choice == 3:
                print(list_user_expenses_ordered_by_categories(file))
            elif choice == 4:
                money = input("New income amount: ")
                category = input("New income type: ")
                date = input("New income date: ")
                add_income(category, money, date, file)
            elif choice == 5:
                money = input("New expense amount: ")
                category = input("New expense type: ")
                date = input("New expense date: ")
                add_expense(category, money, date, file)
            if choice == 6:
                exit()
        finally:
            print()


if __name__ == '__main__':
    main()
