from .movie_controller import MovieController
from .projection_controller import ProjectionController
from .user_controller import UserController
from .reservation_controller import ReservationController
from .utils import NotValidSeat as NotValidSeat
from .utils import SeatNotInRange as SeatNotInRange


def user_exist(func):
    def decorated(username, password):
        if not UserController.is_user(username, password):
            UserController.create(username, password)
        return func(username, password)
    return decorated


class Controller:
    reservations = []
    user_id = None

    @staticmethod
    def create_movie(name, rating):
        try:
            MovieController.create(name, rating)
        except ValueError as e:
            print(e)

    @staticmethod
    def show_movies():
        print(MovieController.show_all_movies())

    @staticmethod
    def create_movie_projection(movie_id, movie_type, date, time):
        ProjectionController.create(movie_id, movie_type, date, time)

    @staticmethod
    def show_movie_projections(movie_id, date=None):
            if date is None:
                print(ProjectionController.show_all_projections(int(movie_id)))
            else:
                print(ProjectionController.show_all_projections_by_date(
                    int(movie_id), date))

    @staticmethod
    @user_exist
    def log_user(username, password):
        if not UserController.is_logged(username, password):
            UserController.logged(username, password)
        Controller.user_id = UserController.get(username, password)

    @staticmethod
    def show_movie_projections_with_avaliable_seats(movie_id):
        print(ProjectionController.show_all_projections_with_avaliable_seats(
            int(movie_id)))

    @staticmethod
    def create_reservation(projection_id, row, column):
        if row > 10 or column > 10 or row < 0 or column < 0:
            raise SeatNotInRange("Lol...NO! Row or column not in range(0, 10)")
        try:
            id = ReservationController.create(
                Controller.user_id, projection_id, row, column)
        except NotValidSeat as e:
            raise e
        else:
            Controller.reservations.append(id)

    @staticmethod
    def give_up():
        for reservation in Controller.reservations:
            ReservationController.delete(reservation)

    @staticmethod
    def check_movie_projection(projection_id, tickets):
        return ReservationController.check_projection_for_avaliable_seats(
            int(projection_id), int(tickets))

    @staticmethod
    def show_projection_reservations(projection_id):
        print(ReservationController.show_all_reservations(int(projection_id)))

    @staticmethod
    def show_projection_spots(projection_id):
        print(ReservationController.show_projection_spots(int(projection_id)))

    @staticmethod
    def show_projection_info(projection_id, seats):
        result = ProjectionController.show_projection_info(projection_id)
        print(result)
        print("Movie: ", result[0], result[1])
        print("Date and Time: ", result[2], result[3], result[4])
        print("Seats: ", *seats)

    @staticmethod
    def finalize():
        ReservationController.finalize(
            Controller.user_id, Controller.reservations)

    @staticmethod
    def cancel_reservation(username):
        ReservationController.cancel_reservation(Controller.user_id)

    @staticmethod
    def exit():
        UserController.log_out(Controller.user_id)
