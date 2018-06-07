import sqlite3
from tabulate import tabulate
import model.queries as queries

DB_NAME = "vehicle_management.db"


class RepairHourProxy:
    @classmethod
    def insert(cls, date, hour):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.insert_repair_hour, (date, hour))
            conn.commit()

    @classmethod
    def add_rapair_hour_for_client(cls, hour_id, vehicle_id, service_id):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.add_repair_hour_for_client,
                      (vehicle_id, service_id, hour_id))
            conn.commit()

    @classmethod
    def update_rapair_hour_for_client(
            cls, hour_id, vehicle_id, service_id):
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

    @classmethod
    def delete_rapair_hour_for_client(cls, hour_id):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.delete_repair_hour_for_client, (hour_id,))
            conn.commit()

    @classmethod
    def list_all_repair_hours(cls):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_repair_hours)
            print("\nREPAIR HOURS")
            return tabulate(res.fetchall(), headers=[
                "id", "date", "hour",
                "vehicle_id", "bill",
                "mechanic_service_id"],
                tablefmt='psql')

    @classmethod
    def list_all_free_hours(cls):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_free_hours)
            print("\nFREE REPAIR HOURS")
            return tabulate(res.fetchall(), headers=["id", "date", "hour"],
                            tablefmt='psql')

    @classmethod
    def list_all_free_hours_by_date(cls, date):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_free_hours_by_date, (date,))
            print(f"\nFREE REPAIR HOURS BY DATE: {date}")
            return tabulate(res.fetchall(), headers=["id", "hour"],
                            tablefmt='psql')

    @classmethod
    def list_all_busy_hours(cls, mechanic):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            m = c.execute(queries.find_user_id,
                          (mechanic.name,)).fetchone()[0]
            res = c.execute(queries.find_all_busy_hours, (m,))
            print("\nBUSY REPAIR HOURS")
            return tabulate(res.fetchall(), headers=["id", "date", "hour"],
                            tablefmt='psql')

    @classmethod
    def list_all_busy_hours_by_date(cls, mechanic, date):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            m = c.execute(queries.find_user_id,
                          (mechanic.name,)).fetchone()[0]
            res = c.execute(queries.find_all_busy_hours_by_date, (date, m))
            print(f"\nBUSY REPAIR HOURS BY DATE: {date}")
            return tabulate(res.fetchall(), headers=["id", "hour"],
                            tablefmt='psql')

    @classmethod
    def update_rapair_hour_for_mechanic(
            cls, hour_id, new_hour, new_bill):
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

    @classmethod
    def find_repair_hour_info_for_client(cls, hour_id):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(
                queries.find_repair_hour_client_info, (hour_id,)).fetchone()
            return f"""
Thank you! You saved an hour on {res[0]} at {res[1]} for {res[2]}!
Vehicle:{res[3]} {res[4]}  with RegNumber: {res[5]}
"""

    @classmethod
    def find_repair_hour_info_for_mechanic(cls, hour_id):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(
                queries.find_repair_hour_mechanic_info, (hour_id,)).fetchone()
            return f"""
On {res[0]} at {res[1]}:
Client: {res[2]}
Vehicle: {res[3]} {res[4]}
Current Bill: {res[5]}$
"""


class UserProxy:
    @classmethod
    def find_user_by_name(cls, name):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_user_id, (name,)).fetchone()
            return res


class ClientProxy:
    @classmethod
    def insert(cls, name, email, phone_number, address=None):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.insert_user,
                      (name, email, phone_number, address))
            res = c.execute(queries.find_user_id, (name,)).fetchone()[0]
            c.execute(queries.insert_client, (res,))
            conn.commit()

    @classmethod
    def list_all_clients(cls):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_clients)
            print("\nCLIENTS")
            return tabulate(res.fetchall(), headers=["id", "name", "email",
                                                     "phone", "address"],
                            tablefmt='psql')

    @classmethod
    def find_client_by_name(cls, name):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_client, (name,)).fetchone()
            return res


class MechanicProxy:
    @classmethod
    def insert(cls, name, email, phone_number, address=None, title=""):
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(queries.insert_user,
                      (name, email, phone_number, address))
            res = c.execute(queries.find_user_id, (name,)).fetchone()[0]
            c.execute(queries.insert_mechanic, (res, title))
            conn.commit()

    @classmethod
    def list_all_mechanics(cls):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_mechanics)
            print("\nMECHANICS")
            return tabulate(res.fetchall(),
                            headers=[
                            "id", "name", "email", "phone",
                            "address", "title"],
                            tablefmt='psql')

    @classmethod
    def find_mechanic_by_name(cls, name):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_mechanic, (name,)).fetchone()
            return res


class MechanicServiceProxy:
    @classmethod
    def insert(cls, mechanic, service_name):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.insert_service, {'name': service_name})
            conn.commit()
            m = c.execute(queries.find_user_id,
                          (mechanic.name,)).fetchone()[0]
            s = c.execute(queries.find_service_id_by_name,
                          (service_name,)).fetchone()[0]
            c.execute(queries.insert_mechanic_service, (m, s))

    @classmethod
    def list_all_services(cls):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_services)
            print("\nSERVICES")
            return tabulate(res.fetchall(), headers=["id", "name"],
                            tablefmt='psql')

    @classmethod
    def list_mechanic_services(cls, mechanic):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            m = c.execute(queries.find_user_id, (mechanic.name,)).fetchone()[0]
            res = c.execute(queries.find_all_mechanic_services, (m,))
            print("\nMECHANIC SERVICES")
            return tabulate(res.fetchall(), headers=["id", "name"],
                            tablefmt='psql')


class VehicleProxy:
    @classmethod
    def insert(cls, owner, category="", make="",
               model="", register_number="", gear_box=""):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_user_id, (owner.name,)).fetchone()[0]
            c.execute(queries.insert_vehicle,
                      (category, make, model,
                       register_number, gear_box, res))

    @classmethod
    def update(cls, vehicle_id, category, make,
               model, register_number, gear_box):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            if category is not None:
                c.execute(queries.update_vehicle_set_category,
                          (category, vehicle_id))
                conn.commit()
            if make is not None:
                c.execute(queries.update_vehicle_set_make,
                          (make, vehicle_id))
                conn.commit()
            if model is not None:
                c.execute(queries.update_vehicle_set_model,
                          (model, vehicle_id))
                conn.commit()
            if register_number is not None:
                c.execute(queries.update_vehicle_set_register_number,
                          (register_number, vehicle_id))
                conn.commit()
            if gear_box is not None:
                c.execute(queries.update_vehicle_set_gear_box,
                          (gear_box, vehicle_id))
                conn.commit()

    @classmethod
    def delete(cls, vehicle_id):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.delete_vehicle, (vehicle_id,))
            conn.commit()

    @classmethod
    def list_all_vehicles(cls):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_vehicles)
            print("\nVEHICLES")
            return tabulate(res.fetchall(),
                            headers=["id", "category", "make", "model",
                                     "register_number", "gear_box",
                                     "owner_name"],
                            tablefmt='psql')

    @classmethod
    def list_vehicles_by_user_name(cls, user_name):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(
                queries.find_all_vehicles_by_user_name, (user_name,))
            print("\nCLIENT VEHICLES")
            return tabulate(res.fetchall(),
                            headers=["id", "category", "make", "model",
                                     "register_number", "gear_box"],
                            tablefmt='psql')
