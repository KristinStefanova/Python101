from controllers.controller import Controller


class Menu:
    controller = Controller()

    @classmethod
    def test_info(cls):
        cls.controller.create_movie("Home Alone", 5.6)
        cls.controller.create_movie("Taxy", 7.6)

        cls.controller.create_movie_projection(1, "3D", '2018-05-23', '19:10')
        cls.controller.create_movie_projection(1, "2D", '2018-05-23', '19:00')
        cls.controller.create_movie_projection(1, "3D", '2018-05-24', '22:15')

        cls.controller.create_movie_projection(2, "2D", '2018-05-23', '18:00')
        cls.controller.create_movie_projection(2, "3D", '2018-05-24', '21:15')

        # user_id = cls.controller.log_user("Krisi", "Krisi125!")

        # print(user_id)
        # tickets = 2
        # movie_id = 1
        # projection_id = 1
        # username = "Krisi"
        # cls.controller.show_movie_projections_with_avaliable_seats(movie_id)
        # print(cls.controller.check_movie_projection(projection_id, tickets))
        # cls.controller.create_reservation(user_id, projection_id, 2, 3)
        # cls.controller.create_reservation(user_id, projection_id, 2, 4)
        # cls.controller.finalize(user_id, username, [1, 2])
        # cls.controller.show_projection_reservations(projection_id)
        # cls.controller.show_projection_spots(projection_id)

        # # GIVE UP exit
        # reservations = []
        # re_id = cls.controller.create_reservation(user_id, projection_id, 2, 3)
        # re_id = cls.controller.create_reservation(user_id, projection_id, 7, 8)
        # reservations.append(re_id)
        # cls.controller.give_up([])
        # re_id = cls.controller.create_reservation(user_id, projection_id, 7, 7)
        # reservations.append(re_id)
        # print(reservations)
        # cls.controller.show_projection_spots(projection_id)

        # seats = [(7, 8), (7, 7)]
        # cls.controller.show_projection_info(projection_id, seats)
        # cls.controller.finalize(user_id, username, reservations)

        # cls.controller.cancel_reservation(username)

    @classmethod
    def start(cls):
        print("Welcome to Krisky Cinema!")
        cls.test_info()

        while True:
            command = input("> ")

            if command == 'show movies':
                cls.controller.show_movies()

            elif command.startswith('show movie projections'):
                movie_id = command.split(' ')[3]
                try:
                    date = command.split(' ')[4]
                except IndexError:
                    cls.controller.show_movie_projections(movie_id)
                else:
                    cls.controller.show_movie_projections(movie_id, date)

            elif command == 'make reservation':
                print("You need to a user in the system to make reservations!")
                username = input("Username: ")
                password = input("Password: ")

                if username == "give up" or password == "give up":
                    break

                try:
                    user_id = cls.controller.log_user(username, password)
                except ValueError:
                    print("Not valid password! Minimum 8 symbols and must include number, symbol, capital leter!")
                    password = input("Password: ")
                    user_id = cls.controller.log_user(username, password)

                print(f"Hello, {username}")

                tickets = input("Step 1 (User): Choose number of tickets> ")

                if tickets == "give up":
                    break

                print("Current movies: \n")
                cls.controller.show_movies()

                movie_id = input("Step 2 (Movie): Choose a movie> ")

                if movie_id == "give up":
                    break

                print("Projections for movie: \n")
                cls.controller.show_movie_projections_with_avaliable_seats(
                    movie_id)

                projection_id = input("Step 3 (Projection): Choose a projection> ")
                if projection_id == "give up":
                    break
                while not cls.controller.check_movie_projection(projection_id, tickets):
                    projection_id = input(
                        "Step 3 (Projection): Choose a projection> ")
                    if projection_id == "give up":
                        break
                print("Available seats (marked with a dot): \n")
                cls.controller.show_projection_spots(projection_id)

                reservations = []
                seats = []
                for i in range(int(tickets)):
                    seat = input(f"Step 4 (Seats): Choose seat {i + 1}> ")
                    if seat == "give up":
                        cls.controller.give_up(reservations)
                        break
                    reservation_id = None
                    seat = (int(seat.split(', ')[0][1:]), int(seat.split(', ')[1][0:-1]))
                    while reservation_id is None:
                        print(user_id, projection_id, seat[0], seat[1])
                        reservation_id = cls.controller.create_reservation(
                            int(user_id), int(projection_id), seat[0], seat[1])
                    reservations.append(reservation_id)
                    seats.append(seat)

                print("This is your reservation: ")
                cls.controller.show_projection_info(projection_id, seats)

                finalize = input("Step 5 (Confirm - type 'finalize')> ")
                if finalize == "give up":
                    cls.controller.give_up(reservations)
                if finalize == "finalize":
                    cls.controller.finalize(
                        user_id, username, password, reservations)

            elif command.startswith('cancel reservation'):
                username = command.split(' ')[2]
                cls.controller.cancel_reservation(username)

            elif command == 'help':
                print("show movies - will show all movies")
                print("show movie projections <movie_id> [<date>] - will show all projections for movie at date(optional)")
                print("make reservation - make new reservation for movie")
                print("cancel reservation <name> - will cancel last reservation of <name>")
                print("help - list all commands")
                print("exit - for exit of application")

            elif command == 'exit':
                break
                exit()
            else:
                print("Not a valid command")
