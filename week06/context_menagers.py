import datetime
from time import sleep, time


class performance:
    def __init__(self, filename):
        self.filename = filename
        self.start = None
        self.end = None
        self.file_handler = None

    def __enter__(self):
        self.start = time()
        self.file_handler = open(self.filename, 'r+')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        diff = self.end - self.start
        self.file_handler.write(
            f"Date {datetime.datetime.now()}. Execution time: {round(diff, 3)}")
        self.file_handler.close()
        return True


with performance("logg.txt"):
    sleep(2)


class assertRaises:
    def __init__(self, exception, msg=""):
        self.exception = exception
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and exc_type == self.exception:
            if self.msg == str(exc_val):
                print(f"{self.exception.__name__}: Exception is raised. Messages are equal!")
            else:
                print(f"{self.exception.__name__}: Exception is raised. Messages are not equal!")
        elif exc_type is not None and exc_type != self.exception:
            print(f"Error. Raised: {self.exception.__name__}")
        else:
            print(f'{self.exception.__name__} is not raised.')
        return True


def do_something():
    raise ValueError("aaaaa")


with assertRaises(ValueError, "aaa"):
    do_something()


