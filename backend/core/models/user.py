from core.models.base import AbstractModel


class User(AbstractModel):
    name: str
    weekly_hours: float
    username: str
    password: str
    email: str
    is_active: bool
