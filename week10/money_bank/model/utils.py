import hashlib


def hashpassword(func):
    def decorated(cls, username, password):
        hashpass = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            username.encode(),
            10000
        ).hex()
        return func(cls, username, hashpass)
    return decorated


def hasNumbers(password):
    return any(char.isdigit() for char in password)


def hasUpper(password):
    return any(char.isupper() for char in password)


def hasSpecialSymbol(password):
    special_symbols = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
    return any(char in special_symbols for char in password)


def password_validation():
    while True:
        password = input("Enter your password: ")
        if len(password) < 8:
            print("Make sure your password is at least 8 letters")
        elif not hasNumbers(password):
            print("Make sure your password contains at least 1 digit")
        elif not hasUpper(password):
            print("Make sure your password contains at least 1 capital letter")
        elif not hasSpecialSymbol(password):
            print("Make sure your password contains at least 1 special_symbols")
        else:
            print("Valid password")
            break
    return password
