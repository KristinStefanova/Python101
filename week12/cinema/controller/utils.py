from hashlib import pbkdf2_hmac
from model.models import Reservation, session
from datetime import datetime


help_command = """
show movies - will show all movies
show movie projections <movie_id> [<date>] - will show all movie projections
make reservation - make new reservation for movie
cancel reservation <name> - will cancel last reservation of <name>
help - list all commands
exit - for exit of application
"""


class NotValidSeat(Exception):
    pass


class SeatNotInRange(Exception):
    pass


class GiveUpException(Exception):
    pass


class NotValidPassword(Exception):
    pass


def has_capital(password):
    return any(char.isupper() for char in password)


def has_special_symbol(password):
    special_symbols = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
    return any(char in special_symbols for char in password)


def validate_password(func):
    def decorated(username, password):
        if len(password) < 8 or not has_capital(
                password) or not has_special_symbol(password):
            raise NotValidPassword("Wrong password")
        return func(username, password)
    return decorated


def hashpassword(func):
    def decorated(username, password):
        hashpass = pbkdf2_hmac(
            'sha256',
            password.encode(),
            username.encode(),
            10000
        ).hex()
        return func(username, hashpass)
    return decorated


class Board:
    @staticmethod
    def create(reserved):
        board = [['.' for i in range(11)]for j in range(11)]
        for i in range(0, 11):
            for j in range(0, 11):
                if i == 0 and j == 0:
                    board[i][j] = None
                if i == 0 and j != 0:
                    board[i][j] = j
                if i != 0 and j == 0:
                    board[i][j] = i
                if (i, j) in reserved:
                        board[i][j] = 'X'
        return board


def log_info(func):
    def decorated(user_id, reservations):
        reservations = ", ".join([f'{res}' for res in reservations])
        info = f"{str(datetime.now())}, {user_id}, "
        with open("log.txt", "a") as file:
            file.write(info + reservations + '\n')
        return func(user_id, reservations)
    return decorated


def find_user_last_reservation(user_id):
    with open("log.txt", "r") as file:
        lines = file.readlines()[-1::]
    for line in lines:
        splitted = line.split(', ')
        if splitted[1] == user_id:
            return [int(item) for item in splitted[3:]]


def check_seat(projection_id, row, column):
    reserved = session.query(Reservation.row, Reservation.col).filter(
        Reservation.projection_id == projection_id).all()
    if (row, column) in reserved:
        raise NotValidSeat("This seat is already taken!")


def custom_input(msg=""):
    option = input(msg)
    if option == 'give up':
        raise GiveUpException
    else:
        return option
