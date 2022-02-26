from django.test import TestCase
from main.models import BaseModel
from django.db import models


class ExampleModel(BaseModel):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)


class TestBaseModel(TestCase):

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
        self.assertEqual(first_name_available_alphabet_letters, {'j', 'f', 'h', 's', 'b'})

        last_name_available_alphabet_letters = ExampleModel.objects.get_available_alphabet_letters(
            field_name='last_name'
        )
        self.assertEqual(last_name_available_alphabet_letters, {'s', 'b', 'p', 'k', 'w'})
