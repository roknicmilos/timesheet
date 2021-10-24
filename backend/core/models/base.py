from abc import ABC, abstractmethod


class AbstractModel(ABC):
    id: int

    objects: 'AbstractManager'


class AbstractManager(ABC):

    @abstractmethod
    def get(self, *, obj_id: int) -> AbstractModel:
        pass

    @abstractmethod
    def create(self, obj: AbstractModel) -> AbstractModel:
        pass

    @abstractmethod
    def update(self, obj: AbstractModel) -> AbstractModel:
        pass

    @abstractmethod
    def delete(self, *, obj_id: int) -> None:
        pass
