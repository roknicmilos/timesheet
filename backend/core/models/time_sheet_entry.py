from core.models.base import AbstractModel
from core.models.daily_time_sheet import DailyTimeSheet
from core.models.project import Project
from core.models.category import Category


class TimeSheetEntry(AbstractModel):
    description: str
    time: float
    overtime: float
    daily_time_sheet: DailyTimeSheet
    project: Project
    category: Category
