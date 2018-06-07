from model.client import Client


class ClientController:
    client = Client()

    @classmethod
    def register(cls, username, password):
        cls.client.register(username, password)

    @classmethod
    def find(cls, username, password):
        return cls.client.find(username, password)

    @classmethod
    def login(cls, username, password):
        cls.client = cls.client.login(username, password)
        return cls

    @classmethod
    def info(cls):
        return f"""
        You are: {cls.client.get_username()}
        Your id is: {cls.client.get_id()}
        Your balance is: {cls.client.get_balance()}
        """

    @classmethod
    def show_username(cls):
        return cls.client.get_username()

    @classmethod
    def show_message(cls):
        return f"Message: {cls.client.get_message()}"

    @classmethod
    def change_message(cls, new_message):
        cls.client.set_message(new_message)

    @classmethod
    def change_password(cls, new_password):
        cls.client.change_password(new_password)
