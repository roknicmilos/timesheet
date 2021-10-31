from core.models.address import Address
from core.models.base import BaseModel


class Client(BaseModel):
    name: str
    address: Address
