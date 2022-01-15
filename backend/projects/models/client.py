from django.db import models
from main.models import BaseModel
from projects.models import Address


class Client(BaseModel):
    name = models.CharField(
        verbose_name='name',
        max_length=250,
    )
    street = models.CharField(
        verbose_name='street',
        max_length=250,
    )
    city = models.CharField(
        verbose_name='city',
        max_length=250,
    )
    country = models.CharField(
        verbose_name='county',
        max_length=250,
    )
    zip_code = models.IntegerField(
        verbose_name='zip code',
    )

    @property
    def address(self) -> Address:
        return Address(
            street=self.street,
            city=self.city,
            zip_code=self.zip_code,
            country=self.country
        )

    def __str__(self):
        return self.name
