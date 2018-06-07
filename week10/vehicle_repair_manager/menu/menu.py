from controller.controllers import UserController
from controller.controllers import ClientController
from controller.controllers import MechanicController


CLIENT_COMMANDS = """
You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
save_repair_hour <hour_id>
update_repair_hour <hour_id>
delete_repair_hour <hour_id>
add_vehicle
update_vehicle <vehicle_id>
delete_vehicle <vehicle_id>
exit
"""

MECHANIC_COMMANDS = """
You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
list_all_busy_hours
list_busy_hours <date>
add_new_repair_hour
add_new_service
update_repair_hour <hour_id>
exit
"""

REPAIR_HOUR_COMMANDS = """
Choose one of the following:
1 - change start hour
2 - change bill
3 - return to main menu
"""


def clientGUI(client):
    while True:
        option = input(CLIENT_COMMANDS)
        if option == "list_all_free_hours":
            print(client.list_all_free_hours())

        elif option.startswith("list_free_hours"):
            print(client.list_free_hours(option.split(' ')[1]))

        elif option.startswith("save_repair_hour"):
            print(client.list_personal_vehicles())
            vehicle = input()
            print(client.list_all_services())
            service = input()
            client.save_repair_hour(option.split(' ')[1], vehicle, service)
            print(client.find_customer_repair_hour_info(
                int(option.split(' ')[1])))

        elif option.startswith("update_repair_hour"):
            vehicle = input(client.list_personal_vehicles())
            service = input(client.list_all_services())
            client.update_repair_hour(
                int(option.split(' ')[1]), vehicle, service)

        elif option.startswith("delete_repair_hour"):
            client.delete_repair_hour(int(option.split(' ')[1]))

        elif option == "add_vehicle":
            category = input("Vehicle category:\n")
            make = input("Vehicle make:\n")
            model = input("Vehicle model:\n")
            register_number = input("Vehicle register number:\n")
            gear_box = input("Vehicle gear box:\n")
            client.add_vehicle(
                category, make, model, register_number, gear_box)
            print("Thank you! You added new personal vehicle!")

        elif option.startswith("update_vehicle"):
            category = input("Vehicle category:\n")
            make = input("Vehicle make:\n")
            model = input("Vehicle model:\n")
            register_number = input("Vehicle register number:\n")
            gear_box = input("Vehicle gear box:\n")
            client.update_vehicle(
                int(option.split(' ')[1]),
                category, make, model, register_number, gear_box)

        elif option.startswith("delete_vehicle"):
            client.delete_vehicle(int(option.split(' ')[1]))

        elif option == "exit":
            exit()

        else:
            raise ValueError("Invalid command!")


def mechanicGUI(mechanic):
    while True:
        option = input(MECHANIC_COMMANDS)
        if option == "list_all_free_hours":
            print(mechanic.list_all_free_hours())

        elif option.startswith("list_free_hours"):
            print(mechanic.list_free_hours(option.split(' ')[1]))

        elif option == "list_all_busy_hours":
            print(mechanic.list_all_busy_hours())

        elif option.startswith("list_busy_hours"):
            print(mechanic.list_busy_hours(option.split(' ')[1]))

        elif option == "add_new_service":
            service_name = input("Provide New service name:\n")
            mechanic.add_new_service(service_name)
            print("Thank you! You added new service!")

        elif option.startswith("add_new_repair_hour"):
            date = input("Repair hour date:\n")
            hour = input("Start hour:\n")
            mechanic.add_new_repair_hour(date, hour)
            print(mechanic.list_all_free_hours())

        elif option.startswith("update_repair_hour"):
            hour = ""
            bill = ""
            while True:
                print(mechanic.find_mechanic_repair_hour_info(
                    option.split(' ')[1]))
                answer = input(REPAIR_HOUR_COMMANDS)
                if answer == "1":
                    hour = input("New hour: ")
                elif answer == "2":
                    bill = input("New bill: ")
                elif answer == "3":
                    break
                else:
                    raise ValueError("Invalid command")
                mechanic.update_repair_hour(
                    option.split(' ')[1], new_hour=hour, new_bill=float(bill))

        elif option == "exit":
            exit()

        else:
            raise ValueError("Invalid command!")


def main():
    user_controller = UserController()
    client_controller = ClientController()
    mechanic_controller = MechanicController()

    name = input("Hello!\n Provide user name:")

    if user_controller.isRegistered(name):
        if client_controller.find(name):
            client = client_controller.create(name)
            clientGUI(client)
        elif mechanic_controller.find(name):
            mechanic = mechanic_controller.create(name)
            mechanicGUI(mechanic)
    else:
        print("Unknown user!\nWould you like to create new user?")
        if input() == "yes":
            user_type = input("Are you a Client or Mechanic?\n")
            user_name = input("Provide user name:\n")
            phone = input("Provide phone number:\n")
            email = input("Provide email:\n")
            address = input("Provide address:\n")
            if user_type == "Client":
                client_controller.add(user_name, email, phone, address)
                client = client_controller.create(user_name)
                clientGUI(client)
            elif user_type == "Mechanic":
                title = input("Provide title\n")
                mechanic_controller.add(
                    user_name, email, phone, address, title)
                mechanic = mechanic_controller.create(user_name)
                mechanicGUI(mechanic)
            else:
                raise ValueError("Incorrect type of user!")
            print(f"""
Thank you, {user_name}!
Welcome to Vehicle Services!
Next time you try to login, provide your user name!
""")
        else:
            exit()
