from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from main.models import BaseModel


class User(AbstractUser, BaseModel):
    name = models.CharField(
        verbose_name='name',
        max_length=250,
        validators=[
            MinLengthValidator(limit_value=4)
        ]
    )
    email = models.EmailField(
        verbose_name='email',
        db_index=True,
        unique=True
    )
    weekly_hours = models.FloatField(
        verbose_name='weekly hours'
    )
    is_admin = models.BooleanField(
        verbose_name='is admin',
        default=False,
    )

    @property
    def is_worker(self) -> bool:
        return not self.is_admin

    def update(self, **kwargs):
        raw_password = kwargs.pop('password', None)
        if raw_password:
            self.set_password(raw_password)
        super(User, self).update(**kwargs)
