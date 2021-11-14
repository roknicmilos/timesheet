from abc import ABC, abstractmethod
from typing import Type
from django.db.models import Model


class AbstractFactory(ABC):
    should_store_in_db: bool = True
    next_id: int = 1
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

        obj = cls.model_class.objects.create(**kwargs) if cls.should_store_in_db else cls.model_class(**kwargs)
        cls.next_id = obj.pk + 1

        return obj

    @classmethod
    def create_batch(cls, count: int, should_store_in_db: bool = None, **kwargs):
        return [cls.create(should_store_in_db=should_store_in_db, **kwargs) for _ in range(count)]

    @classmethod
    def reset(cls) -> None:
        cls.next_id = 1
