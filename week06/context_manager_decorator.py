from time import time, sleep
import datetime
from contextlib import contextmanager


@contextmanager
def performance(filename):
    start = time()

    yield

    end = time()
    diff = end - start
    file_handler = open(filename, 'r+')
    file_handler.write(
        f"Date {datetime.datetime.now()}. Execution time: {round(diff, 3)}")
    file_handler.close()


with performance("logg.txt"):
    sleep(2)


@contextmanager
def assertRaises(exception, msg=""):
    try:
        yield
    except Exception as e:
        if not isinstance(e, exception):
            print(f'Expected {exception.__name__}, got {e.__class__.__name__}')
        if msg:
            if str(e) != msg:
                print(f'Expected {msg}, got {str(e)}')
                raise e
    else:
        print(f'{exception.__name__} is not raised')


def do_something():
    raise TypeError("aaaaa")


with assertRaises(ValueError, "aaaaa"):
    do_something()
