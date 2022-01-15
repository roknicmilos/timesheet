from django.db import models
from main.models import BaseModel


class TimeSheetReport(BaseModel):
    class Meta:
        default_related_name = 'time_sheet_reports'

    hours = models.FloatField(
        verbose_name='hours',
    )
    overtime_hours = models.FloatField(
        verbose_name='overtime hours',
        default=0,
    )
    description = models.TextField(
        verbose_name='description',
        default='',
    )
    daily_time_sheet = models.ForeignKey(
        to='timesheet.DailyTimeSheet',
        verbose_name='daily time sheet',
        on_delete=models.CASCADE,
        related_name='time_sheet_reports',
    )
