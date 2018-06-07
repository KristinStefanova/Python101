import model.queries as queries
from model.utils import hashpassword
import psycopg2

DB_NAME = "dbname=bank2"


class ClientProxy:
    @classmethod
    @hashpassword
    def register(cls, username, password):
        with psycopg2.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(queries.register, (username, password))
            conn.commit()

    @classmethod
    @hashpassword
    def login(cls, username, password):
        with psycopg2.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(queries.login, (username, password))
            result = cursor.fetchone()
            return result

    @classmethod
    @hashpassword
    def find(cls, username, password):
        with psycopg2.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(queries.login, (username, password))
            result = cursor.fetchone()
            return result

    @classmethod
    def change_message(cls, new_message, id):
        with psycopg2.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(queries.update_message, (new_message, id))
            conn.commit()

    @classmethod
    def change_password(cls, new_password, id):
        with psycopg2.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(queries.update_password, (new_password, id))
            conn.commit()
