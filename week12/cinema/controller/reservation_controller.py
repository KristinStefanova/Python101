from model.models import Reservation, session
from tabulate import tabulate
from .utils import check_seat, Board, log_info, find_user_last_reservation


class ReservationController:
    @staticmethod
    def create(user_id, projection_id, row, column):
        check_seat(projection_id, row, column)
        reservation = Reservation(
            user_id=user_id,
            projection_id=projection_id,
            row=row,
            col=column)
        session.add(reservation)
        session.flush()
        session.refresh(reservation)
        return reservation.id

    @staticmethod
    def delete(reservation_id):
        item = session.query(Reservation).filter(
            Reservation.id == reservation_id).one()
        session.delete(item)

    @staticmethod
    def show_all_reservations(projection_id):
        return tabulate(
            session.query(Reservation.projection_id,
                          Reservation.row,
                          Reservation.col).filter(
                Reservation.projection_id == projection_id).all(),
            headers=['projection', 'row', 'column'],
            tablefmt="plain")

    @staticmethod
    def check_projection_for_avaliable_seats(projection_id, tickets):
        avaliable = 100 - session.query(
            Reservation).filter(
            Reservation.projection_id == projection_id).count()
        if tickets > avaliable:
            return False
        else:
            return True

    @staticmethod
    def show_projection_spots(projection_id):
        reserved = session.query(
            Reservation.row, Reservation.col).filter(
            Reservation.projection_id == projection_id).all()
        return tabulate(Board.create(reserved), tablefmt='plain')

    @staticmethod
    @log_info
    def finalize(user_id, reservations):
        session.commit()

    @classmethod
    def cancel_reservation(cls, user_id):
        reservations = find_user_last_reservation(user_id)
        for reservation in reservations:
            cls.delete(reservation)
