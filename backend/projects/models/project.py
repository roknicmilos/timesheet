from django.db import models
from main.models import BaseModel
from main.settings import AUTH_USER_MODEL


class Project(BaseModel):
    name = models.CharField(
        verbose_name='name',
        max_length=250,
    )
    description = models.TextField(
        verbose_name='description',
        default='',
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name='is active',
        default=False,
    )
    is_archived = models.BooleanField(
        verbose_name='is archived',
        default=False,
    )
    lead_employee = models.ForeignKey(
        to=AUTH_USER_MODEL,
        verbose_name='lead employee',
        on_delete=models.SET_NULL,
        null=True,
    )
    client = models.ForeignKey(
        to='projects.Client',
        verbose_name='client',
        on_delete=models.PROTECT,
    )
