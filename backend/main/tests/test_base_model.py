from django.test import TestCase
from django.db import models, IntegrityError
from main.models import BaseModel


class ExampleModel(BaseModel):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=20, unique=True, null=True)


class TestBaseModel(TestCase):

    def tearDown(self) -> None:
        super(TestBaseModel, self).tearDown()
        ExampleModel.objects.all().delete()

    def assertNewExampleModel(self, obj: ExampleModel, **kwargs) -> None:
        self.assertEqual(obj.first_name, kwargs.get('first_name'))
        self.assertEqual(obj.last_name, kwargs.get('last_name'))

    def test_should_return_alphabet_letters_which_are_first_letter_of_string_field_of_existing_objects(self):
        ExampleModel.objects.create(first_name='Jon', last_name='Snow')
        ExampleModel.objects.create(first_name='Frodo', last_name='Baggins')
        ExampleModel.objects.create(first_name='Harry', last_name='Potter')
        ExampleModel.objects.create(first_name='Slevin', last_name='Kelevra')
        ExampleModel.objects.create(first_name='Billy', last_name='Butcher')
        ExampleModel.objects.create(first_name='Bruce', last_name='Wayne')

        first_name_available_alphabet_letters = ExampleModel.objects.get_available_alphabet_letters(
            field_name='first_name'
        )
        self.assertEqual(first_name_available_alphabet_letters, ['b', 'f', 'h', 'j', 's'])

        last_name_available_alphabet_letters = ExampleModel.objects.get_available_alphabet_letters(
            field_name='last_name'
        )
        self.assertEqual(last_name_available_alphabet_letters, ['b', 'k', 'p', 's', 'w'])

    def test_should_create_multiple_model_objects(self):
        kwargs_list = [
            {'first_name': 'Jon', 'last_name': 'Snow'},
            {'first_name': 'Frodo', 'last_name': 'Baggins'},
        ]
        objects = ExampleModel.objects.create_batch(*kwargs_list)
        self.assertEqual(len(objects), len(kwargs_list))
        for obj, kwargs in zip(objects, kwargs_list):
            self.assertNewExampleModel(obj, **kwargs)

    def test_should_not_create_any_model_objects_if_error_is_raised(self):
        self.assertFalse(ExampleModel.objects.exists())
        single_kwargs = {
            'first_name': 'Jon',
            'last_name': 'Snow',
            'email': 'jon@snow.com',
        }

        # Test if kwargs are valid and will create a single object
        obj = ExampleModel.objects.create(**single_kwargs)
        self.assertNewExampleModel(obj, **single_kwargs)
        obj.delete()
        self.assertFalse(ExampleModel.objects.exists())

        kwargs_list = [single_kwargs, single_kwargs]
        # Second kwargs "email" is not unique, and it should raise error:
        try:
            ExampleModel.objects.create_batch(*kwargs_list)
            self.fail('Did not raise IntegrityError')
        except IntegrityError:
            self.assertFalse(ExampleModel.objects.exists())
