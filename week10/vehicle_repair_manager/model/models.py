from model.proxy import VehicleProxy, ClientProxy, MechanicProxy
from model.proxy import UserProxy, MechanicServiceProxy, RepairHourProxy


class User:
    user_proxy = UserProxy()
    repair_hour_proxy = RepairHourProxy()

    @classmethod
    def isRegistered(cls, name):
        return cls.user_proxy.find_user_by_name(name)

    @classmethod
    def list_all_free_hours(cls):
        return cls.repair_hour_proxy.list_all_free_hours()

    @classmethod
    def list_free_hours(cls, date):
        return cls.repair_hour_proxy.list_all_free_hours_by_date(date)


class Client(User):
    client_proxy = ClientProxy()
    repair_hour_proxy = RepairHourProxy()
    vehicle_proxy = VehicleProxy()
    mechanic_service_proxy = MechanicServiceProxy()

    def __init__(self, name="", email="@", phone_number="", address=""):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    @classmethod
    def add(cls, name, email, phone_number, address):
        return cls.client_proxy.insert(name, email, phone_number, address)

    @classmethod
    def find(cls, name):
        return cls.client_proxy.find_client_by_name(name)

    @classmethod
    def create(cls, name):
        return cls(*cls.client_proxy.find_client_by_name(name))

    @classmethod
    def save_repair_hour(cls, hour_id, vehicle_id, service_id):
        return cls.repair_hour_proxy.add_rapair_hour_for_client(
            hour_id, vehicle_id, service_id)

    @classmethod
    def update_repair_hour(cls, hour_id, vehicle=None, service=None):
        return cls.repair_hour_proxy.update_rapair_hour_for_client(
            hour_id, vehicle, service)

    @classmethod
    def delete_repair_hour(cls, hour_id):
        return cls.repair_hour_proxy.delete_rapair_hour_for_client(hour_id)

    def list_personal_vehicles(cls):
        return cls.vehicle_proxy.list_vehicles_by_user_name(cls.name)

    @classmethod
    def find_customer_repair_hour_info(cls, hour_id):
        return cls.repair_hour_proxy.find_repair_hour_info_for_client(hour_id)

    @classmethod
    def list_all_services(cls):
        return cls.mechanic_service_proxy.list_all_services()

    def add_vehicle(self, category, make, model, register_number, gear_box):
        return Client.vehicle_proxy.insert(
            self, category, make, model, register_number, gear_box)

    @classmethod
    def update_vehicle(cls, vehicle_id, category=None, make=None, model=None,
                       register_number=None, gear_box=None):
        return cls.vehicle_proxy.update(
            vehicle_id, category, make, model, register_number, gear_box)

    @classmethod
    def delete_vehicle(cls, vehicle_id):
        return cls.vehicle_proxy.delete(vehicle_id)


class Mechanic(User):
    mechanic_proxy = MechanicProxy()
    repair_hour_proxy = RepairHourProxy()
    mechanic_service_proxy = MechanicServiceProxy()

    def __init__(
            self, name="", email="@", phone_number="", address="", title=""):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.title = title

    @classmethod
    def add(cls, name, email, phone_number, address, title):
        return cls.mechanic_proxy.insert(
            name, email, phone_number, address, title)

    @classmethod
    def find(cls, name):
        return cls.mechanic_proxy.find_mechanic_by_name(name)

    @classmethod
    def create(cls, name):
        return cls(*cls.mechanic_proxy.find_mechanic_by_name(name))

    def list_all_busy_hours(self):
        return Mechanic.repair_hour_proxy.list_all_busy_hours(self)

    def list_busy_hours(self, date):
        return Mechanic.repair_hour_proxy.list_all_busy_hours_by_date(
            self, date)

    @classmethod
    def add_new_repair_hour(cls, date, hour):
        return cls.repair_hour_proxy.insert(date, hour)

    def add_new_service(self, service_name):
        return Mechanic.mechanic_service_proxy.insert(self, service_name)

    @classmethod
    def update_repair_hour(cls, hour_id, new_hour="", new_bill=0):
        return cls.repair_hour_proxy.update_rapair_hour_for_mechanic(
            hour_id, new_hour, new_bill)

    @classmethod
    def find_mechanic_repair_hour_info(cls, hour_id):
        return cls.repair_hour_proxy.find_repair_hour_info_for_mechanic(
            hour_id)
