from main.factories import AbstractFactory
from projects.models import Client


class ClientFactory(AbstractFactory):
    model_class = Client

    @classmethod
    def prepare_kwargs(cls, **kwargs):
        return {
            'name': kwargs.get('name', 'Vega IT'),
            'street': kwargs.get('street', 'Novosadskog Sajma 2'),
            'city': kwargs.get('city', 'Novi Sad'),
            'zip_code': kwargs.get('zip_code', 21000),
            'country': kwargs.get('country', 'Serbia'),
        }
