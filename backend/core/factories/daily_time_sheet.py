from core.factories.base import AbstractFactory
from core.factories.user import UserFactory
from core.factories.utils import get_random_date
from core.models import DailyTimeSheet


class DailyTimeSheetFactory(AbstractFactory):
    model_class = DailyTimeSheet

    @classmethod
    def prepare_kwargs(cls, **kwargs):
        return {
            'date': kwargs.get('date', get_random_date()),
            'employee': kwargs.get('employee', UserFactory.create(should_store_in_db=cls.should_store_in_db)),
        }
