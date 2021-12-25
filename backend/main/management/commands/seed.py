import os
from typing import List
from django.apps import apps
from django.core.management.base import BaseCommand
from importlib import import_module
from django.db.models import Model


class Command(BaseCommand):
    """
    Seeds all objects from the specified apps. Requirement is that app has folder named "seeds"
    that contains .py files that has a list or tuple named "seed_items" with all the objects.
    Objects need to have an attribute "pk". Filenames starting with underscore will be skipped.
    """
    help = 'seeds model objects from the specified apps'

    def add_arguments(self, parser):
        parser.add_argument('apps', nargs='+', help='Names of the apps or "all"')

    def handle(self, *args, **options):
        apps_options = options.get('apps')
        app_configs = self._get_app_configs(apps_options)

        print('Seeding:', app_configs)

        for app_config in app_configs:
            seeds_path = os.path.join(app_config.path, 'seeds')
            if not os.path.isdir(seeds_path):
                continue

            for file in os.listdir(seeds_path):
                if file.startswith('_') or not file.endswith('.py'):
                    continue

                module = import_module(f'{app_config.name}.seeds.{file[:-3]}')
                seed_items = getattr(module, 'seed_items', None)

                if not isinstance(seed_items, (list, tuple)):
                    message = self.style.ERROR(f'{module.__name__} should contain a list of tuple named "seed_items".')
                    self.stdout.write(message)
                    continue

                self._seed_items(seed_items)

    @staticmethod
    def _get_app_configs(apps_options):
        if 'all' in apps_options:
            return apps.get_app_configs()
        return [apps.get_app_config(label) for label in apps_options]

    def _seed_items(self, items_to_seed: List[Model]):
        for item in items_to_seed:
            if not hasattr(item, 'pk'):
                self.stdout.write(self.style.ERROR(f'{item} does not have an attribute "pk".'))
                continue

            model_name = item.__class__.__name__
            if item.__class__.objects.filter(pk=item.pk).exists():
                message = self.style.WARNING(f'{model_name} with ID {item.pk} already exists. Seed is skipped.')
                self.stdout.write(message)
                continue
            try:
                item.save()
                self.stdout.write(self.style.SUCCESS(f'{model_name} {item.pk} created.'))
            except Exception as exception:
                self.stdout.write(self.style.ERROR(exception))
