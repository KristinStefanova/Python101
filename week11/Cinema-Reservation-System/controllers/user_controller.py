from models.models import UserModel


def has_capital(password):
    return any(char.isupper() for char in password)


def has_special_symbol(password):
    special_symbols = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
    return any(char in special_symbols for char in password)


def validate_password(func):
    def decorated(cls, username, password):
        if len(password) < 8 or not has_capital(
                password) or not has_special_symbol(password):
            raise ValueError("Wrong password")
        return func(cls, username, password)
    return decorated


class UserController:
    user = UserModel()

    @classmethod
    @validate_password
    def create(cls, username, password):
        return cls.user.insert(username, password)

    @classmethod
    def get(cls, username, password):
        return cls.user.get_id(username, password)

    @classmethod
    def is_user(cls, username, password):
        print("USER:", cls.user.is_user(username, password))
        return cls.user.is_user(username, password)

    @classmethod
    def is_logged(cls, username, password):
        print("LOGGED:", cls.user.is_logged(username, password))
        return cls.user.is_logged(username, password)

    @classmethod
    def logged(cls, username, password):
        cls.user.logged(username, password)

    @classmethod
    def logged_out(cls, username, password):
        cls.user.logged_out(username, password)
