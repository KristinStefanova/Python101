import unittest
from model.client_proxy import ClientProxy
import database.create_database as create_database
import psycopg2


class ClientProxyTests(unittest.TestCase):

    def setUp(self):
        self.client_proxy = ClientProxy()
        create_database.create()
        self.client_proxy.register('Tester', '123')

    def tearDown(self):
        create_database.drop()

    @classmethod
    def tearDownClass(cls):
        create_database.drop()

    def test_register(self):
        self.client_proxy.register('Dinko', '123123')

        conn = psycopg2.connect(create_database.DB_NAME)
        cursor = conn.cursor()

        cursor.execute(
            """SELECT Count(*)
            FROM clients
            WHERE username = %s AND password = %s
            """, ('Dinko', '123123'))
        users_count = cursor.fetchone()
        self.assertEqual(users_count[0], 1)

        conn.close()

    def test_login(self):
        logged_user_info = self.client_proxy.login('Tester', '123')
        self.assertEqual(logged_user_info[1], 'Tester')

    def test_login_wrong_password(self):
        logged_user_info = self.client_proxy.login('Tester', '123567')
        self.assertEqual(logged_user_info, None)

    def test_change_message(self):
        logged_user_info = self.client_proxy.login('Tester', '123')
        new_message = "podaivinototam"
        self.client_proxy.change_message(new_message, logged_user_info[0])
        logged_user_new_info = self.client_proxy.login('Tester', '123')
        self.assertEqual(logged_user_new_info[3], new_message)

    def test_change_password(self):
        logged_user_info = self.client_proxy.login('Tester', '123')
        new_password = "12345"
        self.client_proxy.change_password(new_password, logged_user_info[0])
        logged_user_new_info = self.client_proxy.login('Tester', new_password)
        self.assertEqual(logged_user_new_info[1], 'Tester')


if __name__ == '__main__':
    unittest.main()
