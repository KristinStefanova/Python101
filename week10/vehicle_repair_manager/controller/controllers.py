from model.models import User, Client, Mechanic


class UserController:
    user = User()

    @classmethod
    def isRegistered(cls, name):
        return cls.user.isRegistered(name)


class ClientController:
    client = Client()

    @classmethod
    def list_all_free_hours(cls):
        return cls.client.list_all_free_hours()

    @classmethod
    def list_free_hours(cls, date):
        return cls.client.list_free_hours(date)

    @classmethod
    def add(cls, name, email, phone_number, address):
        return cls.client.add(name, email, phone_number, address)

    @classmethod
    def find(cls, name):
        return cls.client.find(name)

    @classmethod
    def create(cls, name):
        cls.client = cls.client.create(name)
        return cls

    @classmethod
    def save_repair_hour(cls, hour_id, vehicle_id, service_id):
        return cls.client.save_repair_hour(hour_id, vehicle_id, service_id)

    @classmethod
    def update_repair_hour(cls, hour_id, vehicle=None, service=None):
        return cls.client.update_repair_hour(hour_id, vehicle, service)

    @classmethod
    def delete_repair_hour(cls, hour_id):
        return cls.client.delete_repair_hour(hour_id)

    @classmethod
    def list_personal_vehicles(cls):
        return cls.client.list_personal_vehicles()

    @classmethod
    def find_customer_repair_hour_info(cls, hour_id):
        return cls.client.find_customer_repair_hour_info(hour_id)

    @classmethod
    def list_all_services(cls):
        return cls.client.list_all_services()

    @classmethod
    def add_vehicle(cls, category, make, model, register_number, gear_box):
        return cls.client.add_vehicle(
            category, make, model, register_number, gear_box)

    @classmethod
    def update_vehicle(cls, vehicle_id, category=None, make=None, model=None,
                       register_number=None, gear_box=None):
        return cls.client.update_vehicle(
            vehicle_id, category, make, model, register_number, gear_box)

    @classmethod
    def delete_vehicle(cls, vehicle_id):
        return cls.client.delete_vehicle(vehicle_id)


class MechanicController:
    mechanic = Mechanic()

    @classmethod
    def list_all_free_hours(cls):
        return cls.mechanic.list_all_free_hours()

    @classmethod
    def list_free_hours(cls, date):
        return cls.mechanic.list_free_hours(date)

    @classmethod
    def add(cls, name, email, phone_number, address, title):
        return cls.mechanic.add(name, email, phone_number, address, title)

    @classmethod
    def find(cls, name):
        return cls.mechanic.find(name)

    @classmethod
    def create(cls, name):
        cls.mechanic = cls.mechanic.create(name)
        return cls

    @classmethod
    def list_all_busy_hours(cls):
        return cls.mechanic.list_all_busy_hours(cls)

    @classmethod
    def list_busy_hours(cls, date):
        return cls.mechanic.list_busy_hours(cls, date)

    @classmethod
    def add_new_repair_hour(cls, date, hour):
        return cls.mechanic.add_new_repair_hour(date, hour)

    @classmethod
    def add_new_service(cls, service_name):
        return cls.mechanic.add_new_service(cls, service_name)

    @classmethod
    def update_repair_hour(cls, hour_id, new_hour="", new_bill=0):
        return cls.mechanic.update_repair_hour(
            hour_id, new_hour, new_bill)

    @classmethod
    def find_mechanic_repair_hour_info(cls, hour_id):
        return cls.mechanic.find_customer_repair_hour_info(hour_id)
