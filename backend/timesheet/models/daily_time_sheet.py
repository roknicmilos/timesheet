from django.db import models
from main.models import BaseModel
from main.settings import AUTH_USER_MODEL


class DailyTimeSheet(BaseModel):

    date = models.DateField(
        verbose_name='date',
        unique=True,
    )
    employee = models.ForeignKey(
        to=AUTH_USER_MODEL,
        verbose_name='employee',
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='daily_time_sheets',
    )
