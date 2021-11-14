from typing import List

from django.db import models


class BasePythonModel:
    id: int


class BaseManager(models.Manager):

    # TODO: test atomicity! if one fails, all should fail!
    def create_batch(self, *args) -> List[models.Model]:
        return [self.create(**kwargs) for kwargs in args]


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = BaseManager()

    def update(self, **kwargs):
        for field_name, field_value in kwargs.items():
            setattr(self, field_name, field_value)
        self.save()
