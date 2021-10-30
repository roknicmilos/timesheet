from core.models.base import BaseModel


class User(BaseModel):
    name: str
    weekly_hours: float = 0
    username: str
    email: str
    is_active: bool = True
    is_admin: bool = False

    @property
    def is_worker(self) -> bool:
        return not self.is_admin
