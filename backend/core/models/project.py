from core.models.base import AbstractModel
from core.models.employee import Employee


class Project(AbstractModel):
    name: str
    description: str
    is_active: bool = False
    is_archived: bool = False
    employee: Employee
