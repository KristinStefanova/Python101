# task 01
def count_substrings(haystack, needle):
    counter = 0
    index = 0
    while index < len(haystack):
        if str(haystack[index:index + len(needle)]) == needle:
            counter += 1
            index += len(needle) - 1
        index += 1
    return counter


# print(count_substrings("This is a test string", "is") == 2)
# print(count_substrings("babababa", "baba") == 2)
# print(count_substrings(
#     "Python is an awesome language to program in!", "o") == 4)
# print(count_substrings("We have nothing in common!", "really?") == 0)
# print(count_substrings("This is this and that is this", "this") == 2)


# task 02
def sum_matrix(m):
    return sum([sum([j for j in row]) for row in m])


# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(sum_matrix(m) is 45)

# m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(sum_matrix(m) is 0)

# m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
# print(sum_matrix(m) is 55)


# task 03
def nan_expand(times):
    if times == 0:
        return ""
    if times == 1:
        return "Not a NaN"
    return "Not a " + nan_expand(times - 1)


# print(nan_expand(0) == "")
# print(nan_expand(1) == "Not a NaN")
# print(nan_expand(2) == "Not a Not a NaN")
# print(nan_expand(3) == "Not a Not a Not a NaN")


# task 04
def find_factors(number):
    result = []
    for i in range(2, number + 1):
        if number % i == 0:
            result.append(i)
    return result


# print(find_factors(6))
# print(find_factors(12))
# print(find_factors(16))


def is_prime(number):
    return find_factors(number) == [number]


# print(is_prime(1))
# print(is_prime(21))
# print(is_prime(7))


def prime_factors(number):
    return [factor for factor in find_factors(number) if is_prime(factor)]


# print(prime_factors(6))
# print(prime_factors(12))
# print(prime_factors(16))


def prime_factorization(n):
    result = []
    factors = prime_factors(n)
    copy = n
    power = 0
    for factor in factors:
        while (copy % factor == 0) and (copy != 0):
            power += 1
            copy //= factor
        result.append((factor, power))
        power = 0
        copy = n
    return result


# print(prime_factorization(10) == [(2, 1), (5, 1)])
# print(prime_factorization(14) == [(2, 1), (7, 1)])
# print(prime_factorization(356) == [(2, 2), (89, 1)])
# print(prime_factorization(89) == [(89, 1)])
# print(prime_factorization(1000) == [(2, 3), (5, 3)])


# task 05
def group(things):
    result = []
    count = 0
    index = 0
    while index < len(things):
        for j in range(index, len(things)):
            if things[index] == things[j]:
                count += 1
            else:
                break
        result.append([things[index]] * (count))
        index += count
        count = 0
    return result


# print(group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]])
# print(group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]])


# task 06
def max_consecutive(items):
    items = group(items)
    max_len = len(items[0])
    for item in items:
        if len(item) > max_len:
            max_len = len(item)
    return max_len


# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]) == 4)
# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]) == 3)


# task 07
def read_matrix(rows, columns):
    items = []
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            row.append(input())
        items.append(row)
    return items


def print_matrix(items, rows):
    for i in range(0, rows):
        print(" ".join(items[i]))


def read_matrix_from_file(filename):
    matrix = open(filename).read()
    matrix = [item.split() for item in matrix.split('\n')[:-1]]
    return matrix


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def traverse_matrix(matrix, row, column, word, rows, columns):
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]
    counter = 0
    if matrix[row][column] != word[0]:
        return counter
    for pos in range(0, 8):
        r = row + x[pos]
        c = column + y[pos]
        for k in range(1, len(word) + 1):
            if r >= rows or r < 0 or c >= columns or c < 0 or k >= len(word):
                break
            if matrix[r][c] != word[k]:
                break
            r += x[pos]
            c += y[pos]
        if k == len(word):
            counter += 1
    return counter


def count_words(matrix, rows, columns, word):
    count = 0
    for i in range(0, rows):
        for j in range(0, columns):
            counter = traverse_matrix(matrix, i, j, word, rows, columns)
            if 0 < counter:
                count += counter
    return count


def word_counter(filename):
    word = input()
    matrix = read_matrix_from_file(filename)
    rows = len(matrix)
    columns = len(matrix[0])
    if len(word) > rows or len(word) > columns:
        print("Invalid number of rows or columns!")
        exit()
    if is_palindrome(word):
        return count_words(matrix, rows, columns, word) // 2
    return count_words(matrix, rows, columns, word)


# print(word_counter("matrix.txt") == 3)
# print(word_counter("matrix1.txt") == 3)
# print(word_counter("matrix2.txt") == 4)
# print(word_counter("matrix3.txt") == 3)


# task 08
def gas_stations(distance, tank_size, stations):
    result = []
    stations.append(distance)
    stations.insert(0, 0)
    temp = tank_size
    i = 0
    while i < len(stations) - 1:
        diff = stations[i + 1] - stations[i]
        if temp - diff > 0:
            temp -= diff
        else:
            result.append(stations[i])
            temp = tank_size
            i -= 1
        i += 1
    return result


# print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]) == [
#       80, 140, 220, 290])
# print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]) == [
#       70, 140, 210, 280, 350])
