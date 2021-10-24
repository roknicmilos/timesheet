from datetime import date
from core.models.employee import Employee


class DailyTimeSheet:
    id: int
    date: date
    hours: float = 0
    employee: Employee
