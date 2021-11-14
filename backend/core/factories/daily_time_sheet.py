from datetime import timedelta, date
from typing import List
from django.utils import timezone
from core.factories.base import AbstractFactory
from core.factories import UserFactory
from core.models import DailyTimeSheet


class DailyTimeSheetFactory(AbstractFactory):
    create_model_func = DailyTimeSheet.objects.create
    next_date: date = timezone.now().date()

    @classmethod
    def prepare_kwargs(cls, **kwargs):
        return {
            'date': kwargs.get('date', cls.next_date),
            'employee': kwargs.get('employee', UserFactory.create()),
        }

    @classmethod
    def create(cls, time_sheet_report_count: int = 0, **kwargs):
        daily_time_sheet = super(DailyTimeSheetFactory, cls).create(
            time_sheet_report_count=time_sheet_report_count,
            **kwargs
        )
        cls._create_time_sheet_reports(count=time_sheet_report_count, daily_time_sheets=[daily_time_sheet])
        cls.next_date = daily_time_sheet.date + timedelta(days=1)
        return daily_time_sheet

    @classmethod
    def create_batch(cls, count: int, time_sheet_report_count: int = 0, **kwargs):
        daily_time_sheets = super(DailyTimeSheetFactory, cls).create_batch(count=count, **kwargs)
        if time_sheet_report_count:
            cls._create_time_sheet_reports(count=time_sheet_report_count, daily_time_sheets=daily_time_sheets)

        return daily_time_sheets

    @classmethod
    def _create_time_sheet_reports(cls, count: int, daily_time_sheets: List[DailyTimeSheet]) -> None:
        from core.factories import TimeSheetReportFactory
        for daily_time_sheet in daily_time_sheets:
            TimeSheetReportFactory.create_batch(count=count, daily_time_sheet=daily_time_sheet)

    @classmethod
    def reset(cls) -> None:
        super(DailyTimeSheetFactory, cls).reset()
        cls.next_date = timezone.now().date()
