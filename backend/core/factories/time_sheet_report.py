import random
from core.factories.base import AbstractFactory
from core.factories.daily_time_sheet import DailyTimeSheetFactory
from core.models import TimeSheetReport


class TimeSheetReportFactory(AbstractFactory):
    model_class = TimeSheetReport

    @classmethod
    def prepare_kwargs(cls, **kwargs):
        daily_time_sheet = kwargs.get('daily_time_sheet', DailyTimeSheetFactory.create(
            should_store_in_db=cls.should_store_in_db
        ))
        return {
            'hours': kwargs.get('hours', random.randint(20, 60)),
            'overtime_hours': kwargs.get('overtime_hours', random.randint(5, 20)),
            'description': kwargs.get('description', 'Time sheet report description example'),
            'daily_time_sheet': daily_time_sheet,
        }
