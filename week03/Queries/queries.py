import csv


def read_csv_file(file_name):
    result = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            result.append(row)

    return result


def filter_by_one_agrument(file, column, content):
    result = []
    for row in file:
        if content == row[column]:
            result.append(row)
    return result


def filter_by_one_argument_that_startswith(file, column, startswith):
    result = []
    for row in file:
        if row[column][0:len(startswith)] == startswith:
            result.append(row)
    return result


def filter_by_one_argument_that_contains(file, column, content):
    result = []
    for row in file:
        if content in row[column]:
            result.append(row)
    return result


def filter_by_one_argument_greater_than(file, column, gt):
    result = []
    for row in file:
        if float(row[column]) > gt:
            result.append(row)
    return result


def filter_by_one_argument_less_than(file, column, lt):
    result = []
    for row in file:
        if float(row[column]) < lt:
            result.append(row)
    return result


def filter_by_with_order_by(file, column):
    for i in range(0, len(file) - 1):
        for j in range(i + 1, len(file)):
            if file[i][column].isdigit():
                if float(file[i][column]) > float(file[j][column]):
                    file[i], file[j] = file[j], file[i]
            else:
                if file[i][column].lower() > file[j][column].lower():
                    file[i], file[j] = file[j], file[i]
    return file


def filter(file_name, **kwargs):
    file = read_csv_file(file_name)
    keys = kwargs.keys()
    try:
        header = file[0]
        file = file[1:]
    except Exception as e:
        print(e)
    else:
        for key in keys:
            if key in header:
                file = filter_by_one_agrument(
                    file, header.index(key), kwargs[key])
            else:
                if key == 'order_by':
                    file = filter_by_with_order_by(
                        file, header.index(kwargs[key]))
                else:
                    keyword = key.split('__')[1]
                    k = key.split('__')[0]
                    if keyword == 'startswith':
                        file = filter_by_one_argument_that_startswith(
                            file, header.index(k), kwargs[key])
                    if keyword == 'contains':
                        file = filter_by_one_argument_that_contains(
                            file, header.index(k), kwargs[key])
                    if keyword == 'gt':
                        file = filter_by_one_argument_greater_than(
                            file, header.index(k), kwargs[key])
                    if keyword == 'lt':
                        file = filter_by_one_argument_less_than(
                            file, header.index(k), kwargs[key])
    finally:
        return file


def count(file_name, **kwargs):
    return len(filter(file_name, **kwargs))


def first(file_name, **kwargs):
    return filter(file_name, **kwargs)[0]


def last(file_name, **kwargs):
    return filter(file_name, **kwargs)[len(filter(file_name, **kwargs)) - 1]


def print_file_rows(file):
    if type(file[0]) is str:
        print(", ".join(file))
    else:
        for row in file:
            print(", ".join(row))


def main():
    print_file_rows(filter("empty_file.csv",
                           full_name="Diana Harris", favourite_color="lime"))
    print(count("example_data.csv",
                full_name="Diana Harris", favourite_color="lime"))
    print_file_rows(first("example_data.csv",
                          full_name="Diana Harris", favourite_color="lime"))
    print_file_rows(last("example_data.csv",
                         full_name="Diana Harris", favourite_color="lime"))


if __name__ == '__main__':
    main()
