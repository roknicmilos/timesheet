from django.db import models
from main.models import BaseModel


class Category(BaseModel):
    name = models.CharField(
        verbose_name='name',
        max_length=250,
    )
