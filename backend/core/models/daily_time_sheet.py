from django.db import models
from core.models.base import BaseModel


class DailyTimeSheet(BaseModel):
    class Meta:
        db_table = 'core_daily_time_sheet'

    date = models.DateField(
        verbose_name='date',
        unique=True,
    )
    employee = models.ForeignKey(
        to='core.User',
        verbose_name='employee',
        on_delete=models.CASCADE,
        db_column='user_id',
    )
