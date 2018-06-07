import psycopg2
from .queries import DB_NAME


def atomic(func):
    def decorated(self, *args):
        try:
            return func(self, *args)
        except psycopg2.IntegrityError:
            self.conn.rollback()
        else:
            self.conn.commit()
    return decorated


class Connector:
    def __init__(self):
        self.name = DB_NAME
        self.conn = psycopg2.connect(f"dbname={self.name}")
        self.cursor = self.conn.cursor()

    @atomic
    def execute_query_with_values(self, query, values):
        self.cursor.execute(query, values)
        self.conn.commit()

    @atomic
    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    @atomic
    def all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    @atomic
    def all_values(self, query, values):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    @atomic
    def get(self, query, id):
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()

    @atomic
    def get_values(self, query, values):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    @atomic
    def rollback(self):
        self.conn.rollback()

    @atomic
    def close(self):
        self.conn.close()
