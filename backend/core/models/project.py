from core.models.employee import Employee


class Project:
    id: int
    name: str
    description: str
    is_active: bool = False
    is_archived: bool = False
    employee: Employee
