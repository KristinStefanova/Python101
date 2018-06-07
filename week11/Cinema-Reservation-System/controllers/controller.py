from .movie_controller import MovieController
from .projection_controller import ProjectionController
from .user_controller import UserController
from .reservation_controller import ReservationController


def user_exist(func):
    def decorated(cls, username, password):
        if not UserController.is_user(username, password):
            try:
                UserController.create(username, password)
            except ValueError as e:
                raise e
        return func(cls, username, password)
    return decorated


class Controller:

    @classmethod
    def create_movie(cls, name, rating):
        MovieController.create(name, rating)

    @classmethod
    def show_movies(cls):
        print(MovieController.show_all_movies())

    @classmethod
    def create_movie_projection(cls, movie_id, movie_type, date, time):
        ProjectionController.create(movie_id, movie_type, date, time)

    @classmethod
    def show_movie_projections(cls, movie_id, date=None):
            if date is None:
                print(ProjectionController.show_all_projections(int(movie_id)))
            else:
                print(ProjectionController.show_all_projections_by_date(
                    int(movie_id), date))

    @classmethod
    @user_exist
    def log_user(cls, username, password):
        UserController.logged(username, password)
        return UserController.get(username, password)

    @classmethod
    def show_movie_projections_with_avaliable_seats(cls, movie_id):
        print(ProjectionController.show_all_projections_with_avaliable_seats(
            int(movie_id)))

    @classmethod
    def create_reservation(cls, user_id, projection_id, row, column):
        try:
            id = ReservationController.create(
                user_id, projection_id, row, column)
        except ValueError as e:
            print(e)
        else:
            return id

    @classmethod
    def give_up(cls, reservations):
        for reservation in reservations:
            ReservationController.delete(reservation)

    @classmethod
    def check_movie_projection(cls, projection_id, tickets):
        return ReservationController.check_projection_for_avaliable_seats(
            int(projection_id), int(tickets))

    @classmethod
    def show_projection_reservations(cls, projection_id):
        print(ReservationController.show_all_reservations(int(projection_id)))

    @classmethod
    def show_projection_spots(cls, projection_id):
        print(ReservationController.show_projection_spots(int(projection_id)))

    @classmethod
    def show_projection_info(cls, projection_id, seats):
        result = ProjectionController.show_projection_info(projection_id)[0]
        print("Movie: ", result[0], result[1])
        print("Date and Time: ", result[2], result[3], result[4])
        print("Seats: ", *seats)

    @classmethod
    def finalize(cls, user_id, username, password, reservations):
        ReservationController.finalize(user_id, username, reservations)
        UserController.logged_out(username, password)
        print("Thanks!")

    @classmethod
    def cancel_reservation(cls, username):
        ReservationController.cancel_reservation(username)
