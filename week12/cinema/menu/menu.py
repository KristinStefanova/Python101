from model.models import create
from controller.controller import Controller
from controller.utils import NotValidSeat as NotValidSeat
from controller.utils import SeatNotInRange as SeatNotInRange
from controller.utils import GiveUpException as GiveUpException
from controller.utils import NotValidPassword as NotValidPassword
from controller.utils import custom_input as custom_input, help_command


class Menu:
    controller = Controller()
    create()

    @classmethod
    def test(cls):

        cls.controller.create_movie("Home Alone", 5.6)
        cls.controller.create_movie("Taxy", 7.6)

        cls.controller.create_movie_projection(1, "3D", '2018-05-23', '19:10')
        cls.controller.create_movie_projection(1, "2D", '2018-05-23', '19:00')
        cls.controller.create_movie_projection(1, "3D", '2018-05-24', '22:15')

        cls.controller.create_movie_projection(2, "2D", '2018-05-23', '18:00')
        cls.controller.create_movie_projection(2, "3D", '2018-05-24', '21:15')

        # cls.controller.show_movies()
        # cls.controller.show_movie_projections(1, '2018-05-23')

        # tickets = 2
        # movie_id = 1
        projection_id = 1
        username = "Krisi"
        password = "Krisi125!"

        cls.controller.log_user(username, password)

        # cls.controller.show_movie_projections_with_avaliable_seats(movie_id)
        # print(cls.controller.check_movie_projection(projection_id, tickets))

        cls.controller.create_reservation(projection_id, 2, 3)
        cls.controller.create_reservation(projection_id, 2, 4)

        # cls.controller.show_projection_spots(projection_id)
        # cls.controller.show_projection_info(projection_id, seats)

        cls.controller.finalize()
        cls.controller.exit()

        # tickets = 2
        # movie_id = 1
        # projection_id = 1
        # username = "Krisi"
        # password = "Krisi125!"

        # cls.controller.log_user(username, password)

        # cls.controller.show_movie_projections_with_avaliable_seats(movie_id)

        # print(cls.controller.check_movie_projection(projection_id, tickets))
        # seats = ['(7, 3)', '(7, 4)']
        # cls.controller.create_reservation(projection_id, seats[0])
        # cls.controller.create_reservation(projection_id, seats[1])

        # cls.controller.show_projection_spots(projection_id)
        # cls.controller.show_projection_info(projection_id, seats)

        # cls.controller.finalize()
        # cls.controller.exit()

    @classmethod
    def show_movies(cls):
        cls.controller.show_movies()

    @classmethod
    def show_movie_projections(cls, command):
        movie_id = command.split(' ')[3]
        try:
            date = command.split(' ')[4]
        except IndexError:
            cls.controller.show_movie_projections(movie_id)
        else:
            cls.controller.show_movie_projections(movie_id, date)

    @classmethod
    def log_user(cls):
        print("You need to a user in the system to make reservations!")
        username = custom_input("Username: ")
        password = custom_input("Password: ")
        try:
            cls.controller.log_user(username, password)
        except NotValidPassword as e:
            print("Minimum 8 symbols and number, symbol, capital leter!")
            password = custom_input("Password: ")
            cls.controller.log_user(username, password)

        print(f"Hello, {username}")

    @classmethod
    def get_tickets(cls):
        tickets = custom_input("Step 1 (User): Choose number of tickets> ")

        print("Current movies: \n")
        cls.controller.show_movies()
        return tickets

    @classmethod
    def get_movie(cls):
        movie_id = custom_input("Step 2 (Movie): Choose a movie> ")

        print("Projections for movie: \n")
        cls.controller.show_movie_projections_with_avaliable_seats(
            movie_id)
        return movie_id

    @classmethod
    def get_projection(cls, tickets):
        projection_id = custom_input(
            "Step 3 (Projection): Choose a projection> ")
        while (not cls.controller.check_movie_projection(
            projection_id, tickets)
        ):
            projection_id = custom_input(
                "Step 3 (Projection): Choose a projection> ")

        print("Available seats (marked with a dot): \n")
        cls.controller.show_projection_spots(projection_id)
        return projection_id

    @classmethod
    def get_seats(cls, tickets, projection_id):
        count = 0
        seats = []
        while count < int(tickets):
            seat = custom_input(f"Step 4 (Seats): Choose seat {count + 1}> ")
            if seat == "give up":
                cls.controller.give_up()
                break

            s = (int(seat.split(', ')[0]),
                 int(seat.split(', ')[1]))
            try:
                cls.controller.create_reservation(
                    projection_id, s[0], s[1])
            except (NotValidSeat, SeatNotInRange) as e:
                print(e)
            else:
                seats.append(seat)
                count += 1

        print("This is your reservation: ")
        cls.controller.show_projection_info(projection_id, seats)

    @classmethod
    def finalize(cls):
        finalize = input("Step 5 (Confirm - type 'finalize')> ")
        if finalize == "give up":
            cls.controller.give_up()
        if finalize == "finalize":
            cls.controller.finalize()

    @classmethod
    def cancel_reservation(cls, command):
        username = command.split(' ')[2]
        cls.controller.cancel_reservation(username)

    @classmethod
    def help(cls):
        print(help_command)

    @classmethod
    def exit(cls):
        cls.controller.exit()
        exit()

    @classmethod
    def start(cls):
        print("Welcome to Krisky Cinema!")

        while True:
            command = input("> ")

            if command == 'show movies':
                cls.show_movies()

            elif command.startswith('show movie projections'):
                cls.show_movie_projections()

            elif command == 'make reservation':
                try:
                    cls.log_user()
                    tickets = cls.get_tickets()
                    cls.get_movie()
                    projection_id = cls.get_projection(tickets)
                    cls.get_seats(tickets, projection_id)
                    cls.finalize()
                except GiveUpException:
                    break
            # TO DO make it with name
            elif command.startswith('cancel reservation'):
                cls.cancel_reservation()

            elif command == 'help':
                cls.help()

            elif command == 'exit':
                cls.exit()
            else:
                print("Not a valid command")
