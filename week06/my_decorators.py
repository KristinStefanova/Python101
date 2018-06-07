import datetime
from functools import wraps
from time import sleep, time


def accepts(*types):
    def accepter(func):
        def decorated(*args):
            for i in range(len(args)):
                if type(args[i]) is not types[i]:
                    raise TypeError(
                        f'Argiment {i + 1} of {func.__name__} is not {types[i].__name__}')
            return func(*args)
        return decorated
    return accepter


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


def encrypt(number):
    def accepter(func):
        @wraps(func)
        def decorated():
            result = func()
            final = ""
            for ch in result:
                if ch.isalpha():
                    if ch.isupper():
                        final += chr(((ord(ch) - 64) % 26) + 64 + number)
                    else:
                        final += chr(((ord(ch) - 96) % 26) + 96 + number)
                else:
                    final += ch
            return final
        return decorated
    return accepter


def log(file_name):
    def accepter(func):
        @wraps(func)
        def decorated():
            with open(file_name, 'a') as file:
                file.write(
                    f'{func.__name__} was called at {str(datetime.datetime.now())}\n')
            return func()
        return decorated
    return accepter


def performance(file_name):
    def accepter(func):
        @wraps(func)
        def decorated():
            start = time()
            result = func()
            end = time()
            diff = end - start
            with open(file_name, 'a') as file:
                file.write(
                    f'{func.__name__} was called at and took {round(diff, 3)} seconds to complete.\n')
            return result
        return decorated
    return accepter


@log("log.txt")
@encrypt(2)
def get_low():
    return "Get get get low"


@performance("log1.txt")
def something_heavy():
    sleep(2)
    return "I am done!"


something_heavy()
something_heavy()
something_heavy()

