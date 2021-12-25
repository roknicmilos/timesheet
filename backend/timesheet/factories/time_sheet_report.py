import random
from main.factories import AbstractFactory
from timesheet.factories import DailyTimeSheetFactory
from timesheet.models import TimeSheetReport


class TimeSheetReportFactory(AbstractFactory):
    model_class = TimeSheetReport

    @classmethod
    def prepare_kwargs(cls, **kwargs):
        if 'daily_time_sheet' not in kwargs:
            kwargs['daily_time_sheet'] = DailyTimeSheetFactory.create()
        return {
            'hours': kwargs.get('hours', random.randint(20, 60)),
            'overtime_hours': kwargs.get('overtime_hours', random.randint(5, 20)),
            'description': kwargs.get('description', 'Time sheet report description example'),
            'daily_time_sheet': kwargs.get('daily_time_sheet'),
        }