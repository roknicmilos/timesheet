from core.models.base import AbstractModel


class AbstractUser(AbstractModel):
    name: str
    weekly_hours: float
    username: str
    password: str
    email: str
    is_active: bool

    def __init__(self, **kwargs):
        if self.__class__ is AbstractUser:
            raise Exception(f'{AbstractUser.__name__} cannot be instantiated')
        super(AbstractUser, self).__init__(**kwargs)
