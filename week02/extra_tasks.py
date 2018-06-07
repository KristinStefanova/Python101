# anagrams
def anagrams_help(subject, anagram):
    return len(subject) == len(anagram) and all(
        [True for ch in anagram.lower() if ch in subject.lower()])


def anagrams():
    subject = input("Subject: ")
    anagram = input("Test anagram: ")
    if anagrams_help(subject, anagram):
        return "ANAGRAMS"
    return "NOT ANAGRAMS"


print(anagrams_help("listen", "silent"))
print(anagrams_help("BRADE", "BEARD"))
print(anagrams_help("TOP_CODER", "COTO_PRODE"))
print(anagrams_help("kilata", "cvetelina_yaneva"))


# valid credit card
def to_digits(n):
    return [int(x) for x in str(abs(n))]


def is_credit_card_valid(number):
    number = to_digits(number)
    if len(number) % 2 == 0:
        return False
    result = []
    for i, x in enumerate(number):
        if i % 2 == 0:
            result.append(x)
        else:
            result += (to_digits(x * 2))
    return sum(result) % 10 == 0


print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))


# Goldbach-Conjecture
def is_prime(number):
    if number == 0 or number == 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    return True


def goldbach(n):
    prime_numbers = [x for x in range(1, n) if is_prime(x)]
    result = []
    for x in prime_numbers:
        for y in prime_numbers:
            if x + y == n and x <= y:
                result.append((x, y))
    return result


print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))


matr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matr2 = [[10, 10, 10], [10, 9, 10], [10, 10, 10]]


# Matrix Bombing
def is_position_good(i, j, rows, colums):
    return 0 <= i < rows and 0 <= j < colums


def sum_matrix(m):
    return sum([sum(x) for x in m])


def get_neighbours(matrix, i, j, rows, columns):
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]
    neighbours = []
    for k in range(0, 8):
        if is_position_good(i + x[k], j + y[k], rows, columns):
            neighbours.append((i + x[k], j + y[k]))
    return neighbours


def reduce_all_neighbours(matrix, neighbours, target):
    for x, y in neighbours:
        if matrix[x][y] - target >= 0:
            matrix[x][y] -= target
        else:
            matrix[x][y] = 0
    return matrix


def matrix_bombing_plan(m):
    result = {}
    rows = len(m)
    columns = len(m[0])
    for i in range(0, rows):
        for j in range(0, columns):
            matrix = [x[:] for x in m]
            neighbours = get_neighbours(matrix, i, j, rows, columns)
            matrix = reduce_all_neighbours(matrix, neighbours, matrix[i][j])
            result[(i, j)] = sum_matrix(matrix)
    return result


print(matrix_bombing_plan(matr))
print(matrix_bombing_plan(matr2))


# Reduce file path
def split_path(path):
    result = []
    directory = ""
    for ch in path:
        if ch.isalpha():
            directory += ch
        else:
            result.append(directory)
            result.append(ch)
            directory = ""
        if "" in result:
            result.remove("")
    if directory != "":
        result.append(directory)
    return result


def reduce_file_path(path):
    result_list = split_path(path)
    result = ["/"]
    for i in range(1, len(result_list)):
        if result_list[i] == '/' and len(result) > 0:
            if result[-1] == '/':
                continue
            elif result[-1] == '.':
                result.pop()
            else:
                result.append(result_list[i])
        elif result_list[i] == '.' and len(result) > 1:
            result.pop()
        else:
            result.append(result_list[i])
    if len(result) > 1 and result[-1] == '/':
        result.pop()
    return "".join([item for item in result])


print(reduce_file_path("/"))
print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/www/htdocs/wtf/"))
print(reduce_file_path("/srv/www/htdocs/wtf"))
print(reduce_file_path("/srv/./././././"))
print(reduce_file_path("/etc//wtf/"))
print(reduce_file_path("/etc/../etc/../etc/../"))
print(reduce_file_path("//////////////"))
print(reduce_file_path("/../"))
