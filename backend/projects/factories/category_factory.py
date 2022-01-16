from main.factories import AbstractFactory
from projects.models import Category


class CategoryFactory(AbstractFactory):
    model_class = Category

    @classmethod
    def prepare_kwargs(cls, **kwargs):
        return {
            'name': kwargs.get('name', 'Software Development'),
        }
