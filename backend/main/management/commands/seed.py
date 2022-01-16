import os
from typing import List, Tuple, Type
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

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.seeded_models: List[Type[Model]] = []

    def add_arguments(self, parser):
        parser.add_argument('apps', nargs='+', help='Django app name(s) or "all" for all apps')

    def handle(self, *args, **options):
        app_names = options.get('apps')
        app_configs = self._get_app_configs(app_names)

        self._seed(app_configs=app_configs)
        self._post_seed()


    def _seed(self, app_configs: list) -> None:
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
                self._post_seed_items(module=module)

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
                if seed.__class__ not in self.seeded_models:
                    self.seeded_models.append(seed.__class__)
                self.stdout.write(self.style.SUCCESS(f'{model_name} {seed.pk} created.'))

    def _post_seed_items(self, module) -> None:
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

    def _post_seed(self):
        """
        Sets id column sequence to the correct value for all seeded tables.
        Saving a new model instance that has PK field set to certain value
        will not trigger the update for this sequence, which is why it's
        necessary to set it to the correct value afterwards.
        """

        for model_class in self.seeded_models:
            table_name = model_class._meta.db_table
            try:
                has_applied_fix = self._fix_db_table_id_sequence_if_incorrect(table_name=model_class._meta.db_table)
            except Exception as exception:
                error_message = f'Failed to execute the function for fixing the id (primary key) sequence ' \
                                f'for table "{table_name}" (model {model_class.__name__}):\n{exception}'
                self.stdout.write(self.style.ERROR(error_message))
            else:
                if has_applied_fix:
                    message = f'Fixed id (primary key) sequence for table {table_name} (model {Model})'
                    self.stdout.write(self.style.SUCCESS(message))
                else:
                    message = f'Did not fix id (primary key) sequence for table {table_name} ' \
                              f'(model {Model}) because the sequence is correct'
                    self.stdout.write(message)


    @staticmethod
    def _fix_db_table_id_sequence_if_incorrect(table_name: str) -> bool:
        """Returns True if the fix was applied, and False if the fix was unnecessary and therefore not applied"""

        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT MAX(id) FROM {table_name};")
            results = cursor.fetchall()
            max_id = results[0][0]

            cursor.execute(f"SELECT nextval('{table_name}_id_seq');")
            results = cursor.fetchall()
            next_id = results[0][0]

            if max_id >= next_id:
                cursor.execute(
                    f"SELECT setval('{table_name}_id_seq', COALESCE("
                    f"(SELECT MAX(id)+1 FROM {table_name}), 1"
                    "), false);"
                )
                return True

            return False
