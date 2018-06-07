from models.models import MovieModel
from tabulate import tabulate


class MovieController:
    movie = MovieModel()

    @classmethod
    def create(cls, name, rating):
        if float(rating) < 0:
            raise ValueError("Rating must be positive number")
        cls.movie.insert(name, rating)

    @classmethod
    def show_all_movies(cls):
        return tabulate(
            cls.movie.list_movies(),
            headers=['id', 'title', 'rating'],
            tablefmt="plain")
