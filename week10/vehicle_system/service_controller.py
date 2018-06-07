import sqlite3
from tabulate import tabulate
import user_queries as queries

DB_NAME = "vehicle_management.db"


class MechanicServiceController:
    def insert(self, mechanic, service_name):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.insert_service, (service_name,))
            conn.commit()
            m = c.execute(queries.find_user_id,
                          (mechanic.name,)).fetchone()[0]
            s = c.execute(queries.find_service_id_by_name,
                          (service_name,)).fetchone()[0]
            c.execute(queries.insert_mechanic_service, (m, s))

    def list_all_services(self):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_services)
            print("\nSERVICES")
            return tabulate(res.fetchall(), headers=["id", "name"],
                            tablefmt='psql')

    def list_mechanic_services(self, mechanic):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            m = c.execute(queries.find_user_id, (mechanic.name,)).fetchone()[0]
            res = c.execute(queries.find_all_mechanic_services, (m,))
            print("\nMECHANIC SERVICES")
            return tabulate(res.fetchall(), headers=["id", "name"],
                            tablefmt='psql')
