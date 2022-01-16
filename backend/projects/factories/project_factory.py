from main.factories import AbstractFactory
from projects.factories import ClientFactory
from projects.models import Project


class ProjectFactory(AbstractFactory):
    model_class = Project

    @classmethod
    def prepare_kwargs(cls, **kwargs):
        client = kwargs.get('client') or ClientFactory.create()
        return {
            'name': kwargs.get('name', 'Timesheet'),
            'client': client,
            'description': kwargs.get('description', 'Awesome project'),
            'is_active': kwargs.get('is_active', False),
            'is_archived': kwargs.get('is_archived', False),
            'lead_employee': kwargs.get('lead_employee'),
        }
