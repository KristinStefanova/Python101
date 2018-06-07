from user import User, Mechanic, Client

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
    pass


print("Hello!\n Provide user name:")
name = input()
user = User(name)
find = user.isRegistered()
if find != "Unknown user!":
    if Client().find(name) is not None:
        client = Client().create(name)
        clientGUI(client)
    if Mechanic().find(name) is not None:
        mechanic = Mechanic().create(name)
        mechanicGUI(mechanic)
else:
    print(find)
    print("Would you like to create new user?")
    if input() == "yes":
        user_type = input("Are you a Client or Mechanic?\n")
        user_name = input("Provide user name:\n")
        phone = input("Provide phone number:\n")
        email = input("Provide email:\n")
        address = input("Provide address:\n")
        if user_type == "Client":
            client = Client(user_name, email, phone, address)
            client.add()
            clientGUI(client)
        elif user_type == "Mechanic":
            title = input("Provide title\n")
            mechanic = Mechanic(user_name, email, phone, address, title)
            mechanic.add()
            mechanicGUI(mechanic)
        else:
            raise ValueError("Incorrect type of user!")
        print(f"Thank you, {user_name}!\nWelcome to Vehicle Services!\nNext time you try to login, provide your user name!")
    else:
        exit()

    # one.insert("Sasho", "sasho@sasho.com", "0879531486", "Sofia")
    # two.insert("Sasho2", "sasho2@sasho.com", "0979531486", "Sofia", "bla")
    # cl = Client("Krisi2", "krisi2@krisi.com", "0879531648", "Vratsa")
    # cl.add()
    # print(cl.isRegistered())
    # cl.add_vehicle("Automobile", "Audi", "A3", "X 2564 XX", "Manual")
    # cl.add_vehicle("Automobile", "Opel", "Astra", "X 1741 XX", "Manual")
    # cl.list_personal_vehicles()
    # cl.update_vehicle(2, model="Vectra")
    # cl.list_personal_vehicles()
    # cl.delete_vehicle(2)
    # cl.list_personal_vehicles()

    # mech = Mechanic(
    #     "Baj Krisi", "top@top.com", "0878562265", "Vratsa", "Mnogo qka")
    # mech.add()
    # mech.add_new_service("Oil change")
    # mech.add_new_service("Tires change")
    # mech.add_new_service("Oil filter change")
    # MechanicController().list_all_mechanics()
    # ClientController().list_all_clients()
    # MechanicServiceController().list_all_services()
    # MechanicServiceController().list_mechanic_services(mech)
    # mech.add_new_repair_hour("26-05-2018", "10:20")
    # mech.add_new_repair_hour("25-05-2018", "12:40")
    # mech.add_new_repair_hour("25-05-2018", "10:00")
    # mech.add_new_repair_hour("24-05-2018", "16:00")
    # mech.add_new_repair_hour("27-05-2018", "15:10")
    # RepairHourController().list_all_repair_hours()

    # cl.list_all_free_hours()
    # cl.list_free_hours("25-05-2018")

    # mech.list_all_free_hours()
    # mech.list_free_hours("25-05-2018")

    # cl.save_repair_hour(2, 1, 3)
    # cl.save_repair_hour(1, 1, 1)
    # RepairHourController().list_all_repair_hours()

    # mech.list_all_busy_hours()
    # mech.list_busy_hours("25-05-2018")

    # mech.update_repair_hour(1, new_hour="09:30")
    # RepairHourController().list_all_repair_hours()
    # mech.update_repair_hour(1, new_bill=150)
    # RepairHourController().list_all_repair_hours()
    # cl.update_repair_hour(1, 1, 2)
    # RepairHourController().list_all_repair_hours()
    # cl.delete_repair_hour(1)
    # RepairHourController().list_all_repair_hours()
