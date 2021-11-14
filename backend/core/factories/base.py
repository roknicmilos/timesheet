from abc import ABC, abstractmethod
from typing import Callable


class AbstractFactory(ABC):
    next_id: int = 1
    create_model_func: Callable = None

    def __init_subclass__(cls, **kwargs):
        if not cls.create_model_func:
            raise AttributeError(f'{cls.__name__} class attribute "create_model_func" is missing')

        super(AbstractFactory, cls).__init_subclass__(**kwargs)

    @classmethod
    @abstractmethod
    def prepare_kwargs(cls, **kwargs):
        pass

    @classmethod
    def create(cls, **kwargs):
        kwargs = cls.prepare_kwargs(**kwargs)

        obj = cls.create_model_func(**kwargs)
        cls.next_id = obj.pk + 1

        return obj

    @classmethod
    def create_batch(cls, count: int, **kwargs):
        return [cls.create(**kwargs) for _ in range(count)]

    @classmethod
    def reset(cls) -> None:
        cls.next_id = 1
