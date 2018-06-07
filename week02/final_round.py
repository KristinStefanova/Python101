# task 01
def to_digits(number):
    return [int(d) for d in str(number)]


def is_number_balanced(number):
    digits = to_digits(number)
    if len(digits) <= 1:
        return True
    if len(digits) % 2 == 0:
        return sum(digits[0:(len(digits) // 2)]) == sum(
            digits[(len(digits) // 2):])
    return sum(digits[0:(len(digits) // 2)]) == sum(
        digits[(len(digits) // 2) + 1:])


# print(is_number_balanced(9))
# print(is_number_balanced(4518))
# print(is_number_balanced(28471))
# print(is_number_balanced(1238033))


def increasing_or_decreasing(seq):
    up = 0
    down = 0
    for i in range(0, len(seq) - 1):
        if seq[i] > seq[i + 1]:
            down += 1
        if seq[i] < seq[i + 1]:
            up += 1

    if down == len(seq) - 1:
        return "Down!"
    elif up == len(seq) - 1:
        return "Up!"
    else:
        return False


# print(increasing_or_decreasing([1, 2, 3, 4, 5]))
# increasing_or_decreasing([5, 6, -10])
# increasing_or_decreasing([1, 1, 1, 1])
# increasing_or_decreasing([9, 8, 7, 6])


def get_largest_palindrome(n):
    digits = to_digits(n)
    if len(digits) <= 2:
        if digits[0] <= digits[1]:
            digits[0] -= 1
            digits[1] = digits[0]
    else:
        for i in range(0, len(digits) // 2 - 1):
            digits[len(digits) - i - 1] = digits[i]

        if len(digits) % 2 == 0:
            if digits[len(digits) // 2 - 1] < digits[len(digits) // 2]:
                digits[len(digits) // 2] = digits[len(digits) // 2 - 1]
        else:
            digits[len(digits) // 2] -= 1
    return int("".join([str(digit) for digit in digits]))


# print(get_largest_palindrome(99))
# print(get_largest_palindrome(252))
# print(get_largest_palindrome(994687))
# print(get_largest_palindrome(754649))


def sum_of_numbers(input_string):
    res = []
    digits = "0123456789"
    temp = ""
    for ch in input_string:
        if ch in digits:
            temp += ch
        else:
            res.append(temp)
            temp = ""
    res.append(temp)
    return sum([int(x) for x in res if x != ""])


# print(sum_of_numbers("ab125cd3"))
# print(sum_of_numbers("ab12"))
# print(sum_of_numbers("ab"))
# print(sum_of_numbers("1101"))
# print(sum_of_numbers("1111O"))
# print(sum_of_numbers("1abc33xyz22"))
# print(sum_of_numbers("0hfabnek"))


def birthday_ranges(birthdays, ranges):
    result = []
    temp = 0

    for l, r in ranges:
        for i in range(l, r + 1):
            if i in birthdays:
                temp += birthdays.count(i)
        result.append(temp)
        temp = 0
    return result


# print(birthday_ranges([1, 2, 3, 4, 5], [(
#     1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
# print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(
#     4, 9), (6, 7), (200, 225), (300, 365)]))


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


# task 06
def numbers_to_message(pressed_sequence):
    keyboard = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
                6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    groups = group(pressed_sequence)
    result = ""
    is_cap = False
    for g in groups:
        if g == [0]:
            result += " "
        elif g == [-1]:
            continue
        elif g == [1]:
            is_cap = True
            continue
        else:
            key = g[0]
            letter = keyboard[key][(len(g) - 1) % len(keyboard[key])]
            if is_cap:
                letter = letter.upper()
                is_cap = False
            result += letter
    return result


# print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
# print(numbers_to_message([2, 2, 2, 2]))
# print(numbers_to_message([
#     1, 4, 4, 4, 8, 8, 8, 6, 6,
#     6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def find_group(groups, ch):
    return [group for group in groups if ch in group]


def message_to_numbers(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    keys = [[x] * j for x in range(2, 10) for j in range(1, 4)]
    keys.insert(-8, [7, 7, 7, 7])
    keys.append([9, 9, 9, 9])
    keyboard = {alphabet[i]: keys[i] for i in range(0, len(alphabet))}
    result = [-2]
    for ch in message:
        if ch.isupper():
            result += [1]
            result += keyboard[ch.lower()]
        elif ch.isspace():
            result += [0]
        else:
            last_group = result[-1]
            if last_group in keyboard[ch]:
                result += [-1]
            result += keyboard[ch]
    return result[1:]


# print(message_to_numbers("abc") == [2, -1, 2, 2, -1, 2, 2, 2])
# print(message_to_numbers("a") == [2])
# print(message_to_numbers("Ivo e Panda") == [
#     1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2])
# print(message_to_numbers("aabbcc") == [
#     2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2])


def elevator_trips(
        people_weight, people_floors, elevator_floors, max_people, max_weight):
    if people_floors == [] or people_weight == []:
        return 0
    else:
        counter = 0
        temp_weight = max_weight
        floors = []
        for people, floor in zip(people_weight, people_floors):
            if temp_weight - people >= 0 and len(floors) < max_people:
                temp_weight -= people
                floors.append(floor)
            else:
                counter += len(set(floors)) + 1
                temp_weight = max_weight - people
                floors = []
                floors.append(floor)
        counter += len(set(floors)) + 1
        return counter


# print(elevator_trips([], [], 5, 2, 200))
# print(elevator_trips([40, 50], [], 5, 2, 200))
# print(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))
# print(elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200))
