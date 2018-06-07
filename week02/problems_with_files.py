import sys
from random import randint
import os


def cat(arguments):
    with open(arguments, "r") as f:
        return f.read()


def cat2(arguments):
    for arg in arguments:
        with open(arg, "r") as a:
            print(a.read())
            print()


def generate_numbers(filename, numbers):
    with open(filename, "w") as f:
        for i in range(int(numbers)):
            f.write(str(randint(1, 1000)) + " ")


def sum_numbers(filename):
    with open(filename, "r") as f:
        result = f.read()
    return sum([int(x) for x in result.split()])


def duhs_command(p):
    result = 0
    for root, dirs, files in os.walk(p):
        result += sum([
            os.path.getsize(os.path.join(root, name)) for name in files])
        result += sum([
            os.path.getsize(os.path.join(root, di)) for di in dirs])

    return result / 1024


def dush_command2(p):
    total_size = os.path.getsize(p)
    for item in os.listdir(p):
        itempath = os.path.join(p, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += dush_command2(itempath)
    return total_size


def count_chars(word, filename):
    with open(filename, "r") as a:
        result = a.read()
        if word == "chars":
            return len(result)
        if word == "words":
            return len(result.split())
        if word == "lines":
            return len(result.split('\n'))
