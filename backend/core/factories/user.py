import random
from core.factories.base import AbstractFactory
from core.models import User


class UserFactory(AbstractFactory):
    model_class = User

    @classmethod
    def prepare_kwargs(cls, **kwargs):
        return {
            'email': kwargs.get('email', cls._get_unique_email()),
            'name': kwargs.get('name', 'Jon Snow'),
            'password': kwargs.get('password', 'pass4user'),
            'username': kwargs.get('username', cls._get_unique_username()),
            'weekly_hours': kwargs.get('weekly_hours', random.randint(20, 60))
        }

    @classmethod
    def _get_unique_email(cls) -> str:
        return f'user.{cls._latest_user_id()}@example.com'

    @classmethod
    def _get_unique_username(cls) -> str:
        return f'user.{cls._latest_user_id()}'

    @staticmethod
    def _latest_user_id() -> int:
        try:
            return User.objects.latest('id').pk
        except User.DoesNotExist:
            return 1
