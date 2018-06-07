from vehicle_controller import VehicleController
from user_controller import ClientController, MechanicController
from user_controller import UserController
from service_controller import MechanicServiceController
from repair_hour_controller import RepairHourController


class User:
    def __init__(self, name="", email="@", phone_number="", address=""):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def isRegistered(self):
        return UserController().find_user_by_name(self.name)

    def list_all_free_hours(self):
        return RepairHourController().list_all_free_hours()

    def list_free_hours(self, date):
        return RepairHourController().list_all_free_hours_by_date(date)


class Client(User):
    def __init__(self, name="", email="@", phone_number="", address=""):
        super().__init__(name, email, phone_number, address)

    def add(self):
        return ClientController().insert(
            self.name, self.email, self.phone_number, self.address)

    def find(self, name):
        return ClientController().find_client_by_name(name)

    @classmethod
    def create(cls, name):
        return cls(*ClientController().find_client_by_name(name))

    def save_repair_hour(self, hour_id, vehicle_id, service_id):
        return RepairHourController().add_rapair_hour_for_client(
            hour_id, vehicle_id, service_id)

    def update_repair_hour(self, hour_id, vehicle=None, service=None):
        return RepairHourController().update_rapair_hour_for_client(
            hour_id, vehicle, service)

    def delete_repair_hour(self, hour_id):
        return RepairHourController().delete_rapair_hour_for_client(
            hour_id)

    def list_personal_vehicles(self):
        return VehicleController().list_vehicles_by_user_name(self.name)

    def find_customer_repair_hour_info(self, hour_id):
        return RepairHourController().find_repair_hour_info(hour_id)

    def list_all_services(self):
        return MechanicServiceController().list_all_services()

    def add_vehicle(self, category, make, model, register_number, gear_box):
        return VehicleController().insert(
            self, category, make, model, register_number, gear_box)

    def update_vehicle(self, vehicle_id, category=None, make=None, model=None,
                       register_number=None, gear_box=None):
        return VehicleController().update(
            vehicle_id, category, make, model, register_number, gear_box)

    def delete_vehicle(self, vehicle_id):
        return VehicleController().delete(vehicle_id)


class Mechanic(User):
    def __init__(
            self, name="", email="@", phone_number="", address="", title=""):
        super().__init__(name, email, phone_number, address)
        self.title = title

    def add(self):
        return MechanicController().insert(
            self.name, self.email, self.phone_number, self.address, self.title)

    def find(self, name):
        return MechanicController().find_mechanic_by_name(name)

    @classmethod
    def create(cls, name):
        return cls(*MechanicController().find_mechanic_by_name(name))

    def list_all_busy_hours(self):
        return RepairHourController().list_all_busy_hours(self)

    def list_busy_hours(self, date):
        return RepairHourController().list_all_busy_hours_by_date(self, date)

    def add_new_repair_hour(self, date, hour):
        return RepairHourController().insert(date, hour)

    def add_new_service(self, service_name):
        return MechanicServiceController().insert(self, service_name)

    def update_repair_hour(self, hour_id, new_hour="", new_bill=0):
        return RepairHourController().update_rapair_hour_for_mechanic(
            hour_id, new_hour, new_bill)
