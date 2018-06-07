from model.models import Projection, Reservation, Movie, session
from tabulate import tabulate
from sqlalchemy.sql import func


class ProjectionController:
    @staticmethod
    def create(movie_id, movie_type, date, time):
        session.add(Projection(
            movie_id=movie_id, type=movie_type, date=date, time=time))
        session.commit()

    @staticmethod
    def show_all_projections(movie_id):
        return tabulate(
            session.query(
                Projection.id,
                Projection.date,
                Projection.time,
                Projection.type).filter(
                Projection.movie_id == movie_id).order_by(
                Projection.date).all(),
            headers=['id', 'date', 'time', 'type'],
            tablefmt="plain")

    @staticmethod
    def show_all_projections_by_date(movie_id, date):
        return tabulate(
            session.query(
                Projection.id,
                Projection.time,
                Projection.type).filter(
                Projection.movie_id == movie_id,
                Projection.date == date).order_by(Projection.time).all(),
            headers=['id', 'time', 'type'], tablefmt="plain")

    @staticmethod
    def show_all_projections_with_avaliable_seats(movie_id):
        subquery = session.query(Reservation.projection_id, func.count(
            Reservation.projection_id).label('seats')).group_by(
            Reservation.projection_id).subquery()
        return tabulate(
            session.query(Projection.id,
                          Projection.date,
                          Projection.time,
                          Projection.type,
                          (100 - func.coalesce(subquery.c.seats, 0))
                          ).outerjoin(subquery,
                                      Projection.id == subquery.c.projection_id
                                      ).filter(
                Projection.movie_id == movie_id).all(),
            headers=['id', 'date', 'time', 'type', 'spots'], tablefmt="plain")

    @staticmethod
    def show_projection_info(projection_id):
        return session.query(Movie.name,
                             Movie.rating,
                             Projection.date,
                             Projection.time,
                             Projection.type).filter(
                                Projection.movie_id == Movie.id,
                                Projection.id == projection_id).one()
