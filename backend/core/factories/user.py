from core.factories.base import AbstractFactory
from core.models import User


class UserFactory(AbstractFactory):

    @classmethod
    def create(cls) -> User:
        return User(
            email='jon.snow@winterfell.com',
            name='Jon Snow',
            password='password-101',
            username='username',
        )
