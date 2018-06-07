from model.client_proxy import ClientProxy


class Client():
    client_proxy = ClientProxy()

    def __init__(self, id=None, username=None, balance=0, message=""):
        self.__username = username
        self.__balance = balance
        self.__id = id
        self.__message = message

    @classmethod
    def register(cls, username, password):
        cls.client_proxy.register(username, password)

    @classmethod
    def find(cls, username, password):
        return True if cls.client_proxy.find(username, password) else False

    @classmethod
    def login(cls, username, password):
        return cls(*cls.client_proxy.login(username, password))

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__id

    def get_message(self):
        return self.__message

    def set_message(self, new_message):
        self.__message = new_message
        Client.client_proxy.change_message(new_message, self.__id)

    def change_password(self, new_password):
        Client.client_proxy.change_password(new_password, self.__id)
