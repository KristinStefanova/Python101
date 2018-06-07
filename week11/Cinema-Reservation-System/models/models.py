from hashlib import pbkdf2_hmac
from database.connector import Connector
from database import queries as queries
from datetime import datetime


def hashpassword(func):
    def decorated(cls, username, password):
        hashpass = pbkdf2_hmac(
            'sha256',
            password.encode(),
            username.encode(),
            10000
        ).hex()
        return func(cls, username, hashpass)
    return decorated


def log_info(func):
    def decorated(cls, user_id, username, reservations):
        reservations = ", ".join([f'{res}' for res in reservations])
        info = f"{str(datetime.now())}, {user_id}, {username}, "
        with open("log.txt", "a") as file:
            file.write(info + reservations + '\n')
        return func(cls, user_id, username, reservations)
    return decorated


def find_user_last_reservation(username):
    with open("log.txt", "r") as file:
        lines = file.readlines()[-1::]
    for line in lines:
        splitted = line.split(', ')
        if splitted[2] == username:
            return [int(item) for item in splitted[3:]]


class MovieModel:
    connector = Connector()

    @classmethod
    def insert(cls, name, rating):
        query = queries.INSERT_MOVIE
        cls.connector.execute_query_with_values(query, (name, rating))

    @classmethod
    def list_movies(cls):
        query = queries.LIST_MOVIES
        return cls.connector.all(query)

    @classmethod
    def get_movie(cls, id):
        query = queries.GET_MOVIE_BY_ID
        return cls.connector.get(query, id)


class ProjectionModel:
    connector = Connector()

    @classmethod
    def insert(cls, movie_id, movie_type, date, time):
        query = queries.INSERT_PROJECTION
        cls.connector.execute_query_with_values(
            query, (movie_id, movie_type, date, time))

    @classmethod
    def list_projections(cls, movie_id):
        query = queries.LIST_PROJECTIONS
        return cls.connector.all_values(query, (movie_id, ))

    @classmethod
    def list_projections_by_date(cls, movie_id, date):
        query = queries.LIST_PROJECTIONS_BY_DATE
        return cls.connector.all_values(query, (movie_id, date))

    @classmethod
    def list_projections_with_avaliable_seats(cls, movie_id):
        query = queries.LIST_PROJECTIONS_WITH_AVALIABLE_SEATS
        return cls.connector.all_values(query, (movie_id, ))

    @classmethod
    def list_projection_reserved_spots(cls, projection_id):
        query = queries.LIST_PROJECTION_RESERVED_SEATS
        return cls.connector.all_values(query, (projection_id, ))

    @classmethod
    def show_projection_info(cls, projection_id):
        query = queries.GET_PROJECTION_INFO
        return cls.connector.all_values(query, (projection_id, ))


class Board:

    @classmethod
    def create(cls, reserved):
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


class ReservationModel:
    connector = Connector()

    @classmethod
    def insert(cls, user_id, projection_id, row, column):
        query = queries.INSERT_RESERVATION
        cls.connector.execute_query_with_values(
            query, (user_id, projection_id, row, column))

    @classmethod
    def delete(cls, reservation_id):
        query = queries.DELETE_RESERVATION
        cls.connector.execute_query_with_values(
            query, (reservation_id, ))

    @classmethod
    def get_reservation(cls, user_id, projection_id, row, column):
        query = queries.GET_RESERVATION_ID
        return cls.connector.get_values(
            query, (user_id, projection_id, row, column))[0]

    @classmethod
    def list_reservations(cls, projection_id):
        query = queries.LIST_RESERVATIONS
        return cls.connector.all_values(query, (projection_id, ))

    @classmethod
    def get_projection_reserved_spots(cls, projection_id):
        query = queries.GET_PROJECTION_RESERVED_SPOTS
        return cls.connector.all_values(query, (projection_id, ))

    @classmethod
    def show_projection_spots(cls, projection_id):
        return Board.create(cls.get_projection_reserved_spots(projection_id))

    @classmethod
    @log_info
    def finalize(cls, user_id, username, reservations):
        return True

    @classmethod
    def cancel_reservation(cls, username):
        reservations = find_user_last_reservation(username)
        for reservation in reservations:
            cls.delete(reservation)


class UserModel:
    connector = Connector()

    @classmethod
    @hashpassword
    def insert(cls, username, password):
        query = queries.INSERT_USER
        cls.connector.execute_query_with_values(
            query, (username, password))

    @classmethod
    @hashpassword
    def is_user(cls, username, password):
        query = queries.IS_USER
        return True if cls.connector.get_values(
            query, (username, password)) is not None else False

    @classmethod
    @hashpassword
    def is_logged(cls, username, password):
        query = queries.IS_ACTIVE_USER
        result = cls.connector.get_values(
            query, (username, password))[0]
        return True if result == 1 else False

    @classmethod
    @hashpassword
    def logged(cls, username, password):
        query = queries.SET_ACTIVE_USER
        cls.connector.execute_query_with_values(
            query, (username, password))

    @classmethod
    @hashpassword
    def get_id(cls, username, password):
        query = queries.GET_USER_ID
        return cls.connector.get_values(
            query, (username, password))[0]

    @classmethod
    @hashpassword
    def logged_out(cls, username, password):
        query = queries.SET_NOT_ACTIVE_USER
        cls.connector.execute_query_with_values(
            query, (username, password))
