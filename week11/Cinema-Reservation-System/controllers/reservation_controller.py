from models.models import ReservationModel
from tabulate import tabulate


class ReservationController:
    reservation = ReservationModel()

    @classmethod
    def create(cls, user_id, projection_id, row, column):
        reserved = cls.reservation.get_projection_reserved_spots(projection_id)
        if (row, column) in reserved:
            raise ValueError("This seat is already taken!")
        if row > 10 or column > 10 or row < 0 or column < 0:
            raise ValueError("Lol...NO!")
        else:
            cls.reservation.insert(user_id, projection_id, row, column)
            return cls.reservation.get_reservation(
                user_id, projection_id, row, column)

    @classmethod
    def delete(cls, reservation_id):
        cls.reservation.delete(reservation_id)

    @classmethod
    def show_all_reservations(cls, projection_id):
        return tabulate(
            cls.reservation.list_reservations(projection_id),
            headers=['projection', 'row', 'column'],
            tablefmt="plain")

    @classmethod
    def check_projection_for_avaliable_seats(cls, projection_id, tickets):
        avaliable = 100 - len(cls.reservation.get_projection_reserved_spots(
            projection_id))
        if tickets > avaliable:
            return False
        else:
            return True

    @classmethod
    def show_projection_spots(cls, projection_id):
        return tabulate(cls.reservation.show_projection_spots(
            projection_id), tablefmt='plain')

    @classmethod
    def finalize(cls, user_id, username, reservations):
        cls.reservation.finalize(user_id, username, reservations)

    @classmethod
    def cancel_reservation(cls, username):
        cls.reservation.cancel_reservation(username)
