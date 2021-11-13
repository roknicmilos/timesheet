from abc import ABC, abstractmethod
from typing import Type
from django.db.models import Model


class AbstractFactory(ABC):
    should_store_in_db: bool = True
    model_class: Type[Model]

    @classmethod
    @abstractmethod
    def prepare_kwargs(cls, **kwargs):
        pass

    @classmethod
    def create(cls, should_store_in_db: bool = None, **kwargs):
        if isinstance(should_store_in_db, bool):
            cls.should_store_in_db = should_store_in_db

        kwargs = cls.prepare_kwargs(**kwargs)

        return cls.model_class.objects.create(**kwargs) if cls.should_store_in_db else cls.model_class(**kwargs)


    @classmethod
    def create_batch(cls, size: int, should_store_in_db: bool = None, **kwargs):
        return [cls.create(should_store_in_db=should_store_in_db, **kwargs) for _ in range(size)]
