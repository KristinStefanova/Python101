import time


for i in range(10):
    print(i)

if True:
    return True
else:
    return False


def solution(*args, **kwargs):
    time.sleep(20)


def payment(amount):
    if amount > 10:
        print("Good amount!")
    else:
        print("Bad amount!")
