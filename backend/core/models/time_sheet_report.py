from datetime import date

from core.models.base import BaseModel


class TimeSheetReport(BaseModel):
    date: date
    time: float
    overtime: float
    description: str
    daily_time_sheet_id: int
