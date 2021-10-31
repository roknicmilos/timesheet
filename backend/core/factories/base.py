from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @classmethod
    @abstractmethod
    def create(cls):
        pass

    @classmethod
    def create_batch(cls, size: int):
        return [cls.create() for _ in range(size)]
