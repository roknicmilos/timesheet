from unittest import TestCase
from django.core.exceptions import ValidationError
from core.models import User


class UserTests(TestCase):

    def test_should_raise_validation_error_when_username_is_not_provided(self):
        user = User(username='')
        try:
            user.validate()
        except ValidationError as error:
            self.assertEqual(error.message_dict.get('username')[0], 'Username must be provided')
        else:
            self.fail('Did not raise ValidationError')

    def test_should_raise_validation_error_when_username_is_not_string(self):
        user = User(username=1)
        try:
            user.validate()
        except ValidationError as error:
            self.assertEqual(error.message_dict.get('username')[0], 'Username must be a string')
        else:
            self.fail('Did not raise ValidationError')

    def test_should_raise_validation_error_when_username_is_less_then_4_chars(self):
        user = User(username='u')
        try:
            user.validate()
        except ValidationError as error:
            self.assertEqual(error.message_dict.get('username')[0], 'Username must have at least 4 characters')
        else:
            self.fail('Did not raise ValidationError')

    def test_should_raise_validation_error_when_email_is_not_valid_email(self):
        user = User(email='invalid email')
        try:
            user.validate()
        except ValidationError as error:
            self.assertEqual(error.message_dict.get('email')[0], 'Invalid email')
        else:
            self.fail('Did not raise ValidationError')

    def test_should_raise_validation_error_when_name_is_not_provided(self):
        user = User()
        try:
            user.validate()
        except ValidationError as error:
            self.assertEqual(error.message_dict.get('name')[0], 'Name must be provided')
        else:
            self.fail('Did not raise ValidationError')
