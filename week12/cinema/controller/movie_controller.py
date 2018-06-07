from model.models import Movie, session
from tabulate import tabulate


class MovieController:

    @staticmethod
    def create(name, rating):
        if float(rating) < 0 or float(rating) > 10:
            raise ValueError("Rating must be in (0, 10)")
        session.add(Movie(name=name, rating=rating))
        session.commit()

    @staticmethod
    def show_all_movies():
        return tabulate(
            session.query(Movie.id, Movie.name, Movie.rating).all(),
            headers=['id', 'title', 'rating'],
            tablefmt="plain")

    @staticmethod
    def get_movie(id):
        movie = session.query(Movie).filter(Movie.id == id).one()
        return movie.id
