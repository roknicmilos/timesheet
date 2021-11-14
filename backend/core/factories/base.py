from abc import ABC, abstractmethod
from typing import Type
from django.db.models import Model


class AbstractFactory(ABC):
    next_id: int = 1
    model_class: Type[Model]

    def __init_subclass__(cls, **kwargs):
        if not cls.model_class:
            raise AttributeError(f'{cls.__name__} class attribute "model_class" is missing')

        super(AbstractFactory, cls).__init_subclass__(**kwargs)

    @classmethod
    @abstractmethod
    def prepare_kwargs(cls, **kwargs):
        pass

    @classmethod
    def create(cls, **kwargs):
        kwargs = cls.prepare_kwargs(**kwargs)

        obj = cls.model_class.objects.create(**kwargs)
        cls.next_id = obj.pk + 1

        return obj

    @classmethod
    def create_batch(cls, count: int, **kwargs):
        return [cls.create(**kwargs) for _ in range(count)]

    @classmethod
    def reset(cls) -> None:
        cls.next_id = 1
