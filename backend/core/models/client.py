from core.models.address import Address
from core.models.base import AbstractModel


class Client(AbstractModel):
    name: str
    address: Address
