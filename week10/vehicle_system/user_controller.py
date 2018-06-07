import sqlite3
from tabulate import tabulate
import user_queries as queries

DB_NAME = "vehicle_management.db"


class UserController:
    def find_user_by_name(self, name):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_user_id, (name,)).fetchone()
            if res is None:
                return "Unknown user!"
            else:
                return res[1]


class ClientController:
    def insert(self, name, email, phone_number, address=None):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.insert_user,
                      (name, email, phone_number, address))
            res = c.execute(queries.find_user_id, (name,)).fetchone()[0]
            c.execute(queries.insert_client, (res,))
            conn.commit()

    def list_all_clients(self):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_clients)
            print("\nCLIENTS")
            return tabulate(res.fetchall(), headers=["id", "name", "email",
                                                     "phone", "address"],
                            tablefmt='psql')

    def find_client_by_name(self, name):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_client, (name,)).fetchone()
            return res


class MechanicController:
    def insert(self, name, email, phone_number, address=None, title=""):
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(queries.insert_user,
                      (name, email, phone_number, address))
            res = c.execute(queries.find_user_id, (name,)).fetchone()[0]
            c.execute(queries.insert_mechanic, (res, title))
            conn.commit()

    def list_all_mechanics(self):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_mechanics)
            print("\nMECHANICS")
            return tabulate(res.fetchall(),
                            headers=[
                            "id", "name", "email", "phone",
                            "address", "title"],
                            tablefmt='psql')

    def find_mechanic_by_name(self, name):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_mechanic, (name,)).fetchone()
            return res
