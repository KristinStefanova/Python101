from .connector import Connector
from database.queries import (
    CREATE_TABLE_MOVIES,
    CREATE_TABLE_PROJECTIONS,
    CREATE_TABLE_RESERVATIONS,
    CREATE_TABLE_USERS,
    DROP_TABLE_MOVIES,
    DROP_TABLE_PROJECTIONS,
    DROP_TABLE_RESERVATIONS,
    DROP_TABLE_USERS
)


class Database:
    connector = Connector()

    @classmethod
    def drop(cls):
        cls.connector.execute_query(DROP_TABLE_RESERVATIONS)
        cls.connector.execute_query(DROP_TABLE_USERS)
        cls.connector.execute_query(DROP_TABLE_PROJECTIONS)
        cls.connector.execute_query(DROP_TABLE_MOVIES)

    @classmethod
    def create(cls):
        cls.connector.execute_query(CREATE_TABLE_MOVIES)
        cls.connector.execute_query(CREATE_TABLE_PROJECTIONS)
        cls.connector.execute_query(CREATE_TABLE_USERS)
        cls.connector.execute_query(CREATE_TABLE_RESERVATIONS)

    @classmethod
    def close(cls):
        cls.connector.close()
