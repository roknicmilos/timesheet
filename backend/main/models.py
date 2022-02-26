import string
from typing import List, Set
from django.db import models, transaction
from django_extensions.db.models import TimeStampedModel


class BaseManager(models.Manager):

    @transaction.atomic
    def create_batch(self, *args) -> List[models.Model]:
        return [self.create(**kwargs) for kwargs in args]

    def get_available_alphabet_letters(self, field_name: str) -> Set[str]:
        available_alphabet_letters = set()

        all_alphabet_letters = list(string.ascii_lowercase)
        for letter in all_alphabet_letters:
            filters = {f'{field_name}__istartswith': letter}
            if self.filter(**filters).exists():
                available_alphabet_letters.add(letter)

        return available_alphabet_letters


class BaseModel(TimeStampedModel):
    class Meta:
        abstract = True

    objects = BaseManager()

    def update(self, **kwargs):
        for field_name, field_value in kwargs.items():
            setattr(self, field_name, field_value)
        self.save()
