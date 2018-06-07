from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(
        Float, CheckConstraint('rating>=1 and rating<=10'), default=0)


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id), nullable=False)
    type = Column(String)
    date = Column(String)
    time = Column(String)
    movie = relationship("Movie", backref="projections")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Integer, default=0)


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    projection_id = Column(Integer, ForeignKey(Projection.id), nullable=False)
    row = Column(Integer, CheckConstraint('row>=1 and row<=10'))
    col = Column(Integer, CheckConstraint('col>=1 and col<=10'))
    user = relationship("User", backref="reservations")
    projection = relationship("Projection", backref="reservations")


engine = create_engine("sqlite:///cinema.db")
Session = sessionmaker(engine)
session = Session()


def create():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
