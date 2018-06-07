def sum_of_digits(n):
    if type(n) is not int:
        raise TypeError
    return sum([int(x) for x in str(abs(n))])


def to_digits(n):
    if type(n) is not int:
        raise TypeError
    return [int(x) for x in str(abs(n))]


def to_number(digits):
    if type(digits) is not list:
        raise TypeError
    if any([True for x in digits if type(x) is not int]):
        raise ValueError
    return int("".join([str(digit) for digit in digits]))


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fact_digits(n):
    if type(n) is not int:
        raise TypeError
    if n < 0:
        raise ValueError
    return sum(map(factorial, to_digits(n)))


def fibonacci_function(n):
    if n <= 2:
        return 1
    return fibonacci_function(n - 1) + fibonacci_function(n - 2)


def fibonacci(n):
    if type(n) is not int:
        raise TypeError
    if n < 0:
        raise ValueError
    return [fibonacci_function(x) for x in range(1, n + 1)]


def fib_number(n):
    if type(n) is not int:
        raise TypeError
    if n < 0:
        raise ValueError
    return to_number(fibonacci(n))


def palindrome(n):
    if type(n) is not int and type(n) is not str:
        raise TypeError
    return str(n) == str(n)[::-1]


def count_vowels(st):
    if type(st) is not str:
        raise TypeError
    st = st.lower()
    vowels = "aeiouy"
    return sum([1 for x in st.lower() if x in vowels])


def count_consonants(st):
    if type(st) is not str:
        raise TypeError
    st = st.lower()
    consonants = "bcdfghjklmnpqrstvwxz"
    return sum([1 for x in st.lower() if x in consonants])


def count_occurrences(ch, string):
    return sum([1 for x in string if x == ch])


def char_histogram(string):
    if type(string) is not str:
        raise TypeError
    return {x: count_occurrences(x, string) for x in string}
