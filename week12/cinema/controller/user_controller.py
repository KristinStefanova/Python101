from model.models import User, session
from .utils import validate_password, hashpassword


class UserController:
    @staticmethod
    @validate_password
    @hashpassword
    def create(username, password):
        session.add(User(username=username, password=password))
        session.commit()

    @staticmethod
    @hashpassword
    def get(username, password):
        user = session.query(User).filter(
            User.username == username, User.password == password).one()
        return user.id

    @staticmethod
    @hashpassword
    def is_user(username, password):
        try:
            session.query(User).filter(
                User.username == username, User.password == password).one()
        except Exception:
            return False
        else:
            return True

    @staticmethod
    @hashpassword
    def is_logged(username, password):
        user = session.query(User).filter(
            User.username == username, User.password == password).one()
        return True if user.is_active == 1 else False

    @staticmethod
    @hashpassword
    def logged(username, password):
        user = session.query(User).filter(
            User.username == username, User.password == password).one()
        user.is_active = 1
        session.commit()

    @staticmethod
    def log_out(user_id):
        user = session.query(User).filter(
            User.id == user_id).one()
        user.is_active = 0
        session.commit()
