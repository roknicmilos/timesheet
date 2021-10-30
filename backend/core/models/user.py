from django.core.validators import MinLengthValidator, EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    objects = None

    name = models.CharField(
        verbose_name=_('name'),
        max_length=250,
        validators=[
            MinLengthValidator(limit_value=3),
        ],
    )
    weekly_hours = models.FloatField(
        verbose_name=_('weekly hours'),
        default=0,
    )
    username = models.CharField(
        verbose_name=_('username'),
        max_length=250,
        validators=[
            MinLengthValidator(limit_value=3),
        ],
    )
    email = models.CharField(
        verbose_name=_('email'),
        max_length=250,
        validators=[
            EmailValidator(),
        ],
    )
    is_active = models.BooleanField(
        verbose_name=_('is active'),
        default=True,
    )
    is_admin = models.BooleanField(
        verbose_name=_('is admin'),
        default=False,
    )

    @property
    def is_worker(self) -> bool:
        return not self.is_admin
