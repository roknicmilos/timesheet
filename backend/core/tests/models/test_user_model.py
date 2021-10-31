from unittest import TestCase
from django.core.exceptions import ValidationError
from core.models import User


class UserTests(TestCase):

    def assertValidationError(self, user: User, field_name: str, expected_message: str) -> None:
        user.password = 'valid-password-101'  # to avoid raising an error due to invalid password
        try:
            user.validate()
        except ValidationError as error:
            field_error = error.message_dict.get(field_name)
            if field_error:
                self.assertEqual(field_error[0], expected_message)
            else:
                self.fail(
                    f'ValidationError for "{field_name}" field is missing. '
                    f'Expected error message: "{expected_message}"'
                )
        else:
            self.fail(
                f'Did not raise ValidationError for "{field_name}" field. '
                f'Expected error message: "{expected_message}"'
            )

    def test_should_raise_validation_error_when_username_is_not_provided(self):
        user = User(username='')
        self.assertValidationError(user=user, field_name='username', expected_message='Username must be provided')

    def test_should_raise_validation_error_when_username_is_not_string(self):
        user = User(username=1)
        self.assertValidationError(user=user, field_name='username', expected_message='Username must be a string')

    def test_should_raise_validation_error_when_username_is_less_then_4_chars(self):
        user = User(username='u')
        self.assertValidationError(
            user=user,
            field_name='username',
            expected_message='Username must have at least 4 characters'
        )

    def test_should_raise_validation_error_when_email_is_not_valid_email(self):
        user = User(email='invalid email')
        self.assertValidationError(user=user, field_name='email', expected_message='Invalid email')

    def test_should_raise_validation_error_when_name_is_not_provided(self):
        user = User()
        self.assertValidationError(user=user, field_name='name', expected_message='Name must be provided')

    def test_should_return_false_when_password_is_incorrect(self):
        password = 'password1234'
        user = User(password=password)
        is_correct_password = user.check_password(raw_password=f'incorrect{password}')
        self.assertFalse(is_correct_password)

    def test_should_return_true_when_password_is_correct(self):
        password = 'password1234'
        user = User(password=password)
        is_correct_password = user.check_password(raw_password=password)
        self.assertTrue(is_correct_password)
