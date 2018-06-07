from menu import menu
import database.create_database as create_database


def main():
    create_database.create()
    menu.main_menu()


if __name__ == '__main__':
    main()

# TODO: TEST FOR PASSWORD VALIDATION IN PROXY
# TODO: TEST FOR SQL INJECTION
# TODO: REPAIR PROXY TEST
# TODO: https://docs.python.org/3.4/library/getpass.html#getpass.getpass