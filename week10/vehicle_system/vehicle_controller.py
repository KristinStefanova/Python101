import sqlite3
from tabulate import tabulate
import user_queries as queries

DB_NAME = "vehicle_management.db"


class VehicleController:
    def insert(self, owner, category="", make="",
               model="", register_number="", gear_box=""):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_user_id, (owner.name,)).fetchone()[0]
            c.execute(queries.insert_vehicle,
                      (category, make, model,
                       register_number, gear_box, res))

    def update(self, vehicle_id, category, make,
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

    def delete(self, vehicle_id):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(queries.delete_vehicle, (vehicle_id,))
            conn.commit()

    def list_all_vehicles(self):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(queries.find_all_vehicles)
            print("\nVEHICLES")
            return tabulate(res.fetchall(),
                            headers=["id", "category", "make", "model",
                                     "register_number", "gear_box",
                                     "owner_name"],
                            tablefmt='psql')

    def list_vehicles_by_user_name(self, user_name):
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            res = c.execute(
                queries.find_all_vehicles_by_user_name, (user_name,))
            print("\nCLIENT VEHICLES")
            return tabulate(res.fetchall(),
                            headers=["id", "category", "make", "model",
                                     "register_number", "gear_box"],
                            tablefmt='psql')
