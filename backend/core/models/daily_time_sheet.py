from core.models.base import BaseModel
from datetime import date


class DailyTimeSheet(BaseModel):
    date: date
    employee_id: int
