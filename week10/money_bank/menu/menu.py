from controller.client_controller import ClientController
from model.utils import password_validation


def main_menu():

    print("""
Welcome to our bank service. You are not logged in.
Please register or login""")

    while True:
        client_controller = ClientController()
        command = input("$$$> ")

        if command == 'register':
            username = input("Enter your username: ")
            password = password_validation()

            client_controller.register(username, password)

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if client_controller.find(username, password):
                logged_user = client_controller.login(username, password)
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.show_username())
    while True:
        command = input("Logged>> ")

        if command == 'info':
            print(logged_user.info())

        elif command == 'changepass':
            new_password = password_validation()
            logged_user.change_password(new_password)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            logged_user.change_message(new_message)

        elif command == 'show-message':
            print(logged_user.show_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")
