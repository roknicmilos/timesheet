from datetime import date
from django.db import models
from auth.models import User
from main.models import BaseModel
from projects.models import Client


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
    project = models.ForeignKey(
        to='projects.Project',
        verbose_name='project',
        on_delete=models.PROTECT,
        related_name='time_sheet_reports',
    )
    category = models.ForeignKey(
        to='projects.Category',
        verbose_name='category',
        on_delete=models.PROTECT,
        related_name='time_sheet_reports',
    )

    @property
    def employee(self) -> User:
        return self.daily_time_sheet.employee

    @property
    def client(self) -> Client:
        return self.project.client

    @property
    def date(self) -> date:
        return self.daily_time_sheet.date
