from models.models import ProjectionModel
from tabulate import tabulate


class ProjectionController:
    projection = ProjectionModel()

    @classmethod
    def create(cls, movie_id, movie_type, date, time):
        # if float(rating) < 0:
        #     raise ValueError("Rating must be positive number")
        cls.projection.insert(movie_id, movie_type, date, time)

    @classmethod
    def show_all_projections(cls, movie_id):
        return tabulate(
            cls.projection.list_projections(movie_id),
            headers=['id', 'date', 'time', 'type'],
            tablefmt="plain")

    @classmethod
    def show_all_projections_by_date(cls, movie_id, date):
        return tabulate(
            cls.projection.list_projections_by_date(movie_id, date),
            headers=['id', 'time', 'type'], tablefmt="plain")

    @classmethod
    def show_all_projections_with_avaliable_seats(cls, movie_id):
        return tabulate(
            cls.projection.list_projections_with_avaliable_seats(movie_id),
            headers=['id', 'date', 'time', 'type', 'spots'], tablefmt="plain")

    @classmethod
    def show_projection_info(cls, projection_id):
        return cls.projection.show_projection_info(projection_id)
