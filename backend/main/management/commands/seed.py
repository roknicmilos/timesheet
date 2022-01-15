import os
from typing import List, Tuple
from importlib import import_module
from django.apps import apps
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.models import Model


class Command(BaseCommand):
    """
    Seeds all objects from the specified Django apps.

    Requirement is that apps has folder named "seeds" that contains .py files that
    have a collection (list or tuple) named "seed_items" with all the objects.

    If defined, function "post_seed" will be executed after "seed_items" from the same
    file are seeded. This function can be used for handling Many-to-Many relationships.

    Objects need to have an attribute "pk", because it will be checked if the object
    with the specified "pk" exists, and it will be created only if it doesn't exist.

    Filenames starting with underscore (e.g. _my_file.py) will be skipped.

    If you want to seed all apps, but in a specific order, you can define SEEDS_ORDER tuple
    in settings.py that will contain app names in the desired order.
    """

    help = 'seeds model objects from the specified Django apps'

    def add_arguments(self, parser):
        parser.add_argument('apps', nargs='+', help='Django app name(s) or "all" for all apps')

    def handle(self, *args, **options):
        app_names = options.get('apps')
        app_configs = self._get_app_configs(app_names)

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
                    error_message = self.style.ERROR(
                        f'{module.__name__} should contain a list of tuple named "seed_items".'
                    )
                    self.stdout.write(error_message)
                    continue

                self._seed_items(seed_items=seed_items)
                self._run_post_seed(module=module)

    @classmethod
    def _get_app_configs(cls, apps_options) -> list:
        if 'all' in apps_options:
            if seeds_order := getattr(settings, 'SEEDS_ORDER', None):
                return cls._get_ordered_app_configs(app_names=seeds_order)
            return apps.get_app_configs()
        return [apps.get_app_config(app_name) for app_name in apps_options]

    @staticmethod
    def _get_ordered_app_configs(app_names: Tuple[str]) -> list:
        app_configs = [apps.get_app_config(app_name) for app_name in app_names]
        for app_config in apps.get_app_configs():
            if app_config not in app_configs:
                app_configs.append(app_config)
        return app_configs

    def _seed_items(self, seed_items: List[Model]) -> None:
        for seed in seed_items:
            if not hasattr(seed, 'pk'):
                self.stdout.write(self.style.ERROR(f'{seed} does not have an attribute "pk".'))
                continue

            model_name = seed.__class__.__name__
            if seed.__class__.objects.filter(pk=seed.pk).exists():
                warning_message = self.style.WARNING(
                    f'{model_name} with ID {seed.pk} already exists. Seed is skipped.'
                )
                self.stdout.write(warning_message)
                continue

            try:
                seed.save()
            except Exception as exception:
                error_message = f'Failed to seed the item of type {seed.__class__.__name__} ' \
                                f'with PK {seed.pk}:\n{exception}'
                self.stdout.write(self.style.ERROR(error_message))
            else:
                self.stdout.write(self.style.SUCCESS(f'{model_name} {seed.pk} created.'))

    def _run_post_seed(self, module) -> None:
        post_seed = getattr(module, 'post_seed', None)
        if callable(post_seed):
            try:
                post_seed()
            except Exception as exception:
                error_message = f'Failed to execute "post_seed" callable from {module.__name__}:\n{exception}'
                self.stdout.write(self.style.ERROR(error_message))
            else:
                message = f'Successfully executed "post_seed" callable from {module.__name__}'
                self.stdout.write(self.style.SUCCESS(message))
