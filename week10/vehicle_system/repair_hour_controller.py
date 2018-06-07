import sqlite3
from tabulate import tabulate
import user_queries as queries

DB_NAME = "vehicle_management.db"


class RepairHourController:
    def insert(self, date, hour):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.insert_repair_hour, (date, hour))
            conn.commit()

    def add_rapair_hour_for_client(self, hour_id, vehicle_id, service_id):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.add_repair_hour_for_client,
                      (vehicle_id, service_id, hour_id))
            conn.commit()

    def update_rapair_hour_for_client(
            self, hour_id, vehicle_id, service_id):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            if vehicle_id is not None:
                c.execute(queries.update_repair_hour_for_client_set_vehicle,
                          (vehicle_id, hour_id))
                conn.commit()
            if service_id is not None:
                c.execute(queries.update_repair_hour_for_client_set_service,
                          (service_id, hour_id))
                conn.commit()

    def delete_rapair_hour_for_client(self, hour_id):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.delete_repair_hour_for_client, (hour_id,))
            conn.commit()

    def list_all_repair_hours(self):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_repair_hours)
            print("\nREPAIR HOURS")
            return tabulate(res.fetchall(), headers=[
                "id", "date", "hour",
                "vehicle_id", "bill",
                "mechanic_service_id"],
                tablefmt='psql')

    def list_all_free_hours(self):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_free_hours)
            print("\nFREE REPAIR HOURS")
            return tabulate(res.fetchall(), headers=["id", "date", "hour"],
                            tablefmt='psql')

    def list_all_free_hours_by_date(self, date):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_free_hours_by_date, (date,))
            print(f"\nFREE REPAIR HOURS BY DATE: {date}")
            return tabulate(res.fetchall(), headers=["id", "hour"],
                            tablefmt='psql')

    def list_all_busy_hours(self, mechanic):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            m = c.execute(queries.find_user_id,
                          (mechanic.name,)).fetchone()[0]
            res = c.execute(queries.find_all_busy_hours, (m,))
            print("\nBUSY REPAIR HOURS")
            return tabulate(res.fetchall(), headers=["id", "date", "hour"],
                            tablefmt='psql')

    def list_all_busy_hours_by_date(self, mechanic, date):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            m = c.execute(queries.find_user_id,
                          (mechanic.name,)).fetchone()[0]
            res = c.execute(queries.find_all_busy_hours_by_date, (date, m))
            print(f"\nBUSY REPAIR HOURS BY DATE: {date}")
            return tabulate(res.fetchall(), headers=["id", "hour"],
                            tablefmt='psql')

    def update_rapair_hour_for_mechanic(
            self, hour_id, new_hour, new_bill):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            if new_hour != "":
                c.execute(queries.update_repair_hour_for_mechanic_set_hour,
                          (new_hour, hour_id))
                conn.commit()
            if new_bill != 0:
                c.execute(queries.update_repair_hour_for_mechanic_set_bill,
                          (new_bill, hour_id))
                conn.commit()

    def find_repair_hour_info(self, hour_id):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(
                queries.find_repair_hour_info, (hour_id,)).fetchone()
            return f"Thank you! You saved an hour on {res[0]} at {res[1]} for {res[2]}!\nVehicle:{res[3]} {res[4]}  with RegNumber: {res[5]}"
