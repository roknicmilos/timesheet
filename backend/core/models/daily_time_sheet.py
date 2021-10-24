from datetime import date

from core.models.base import AbstractModel
from core.models.employee import Employee


class DailyTimeSheet(AbstractModel):
    date: date
    hours: float = 0
    employee: Employee
