from unittest import TestCase
from django.core.exceptions import ValidationError
from core.utils import validate_raw_password


class ValidateRawPasswordTests(TestCase):

    def assertRawPasswordValidationError(self, raw_password: str, expected_message: str) -> None:
        try:
            validate_raw_password(raw_password=raw_password)
        except ValidationError as error:
            self.assertEqual(error.message, expected_message)
        else:
            self.fail(f'Did not raise ValidationError. Expected error message: {expected_message}')

    def test_should_raise_validation_error_if_password_is_not_provided(self):
        self.assertRawPasswordValidationError(
            raw_password='',
            expected_message='Password must be provided'
        )

    def test_should_raise_validation_error_if_password_is_less_then_8_chars(self):
        self.assertRawPasswordValidationError(
            raw_password='pass',
            expected_message='Password must be at least 8 characters long'
        )

    def test_should_raise_validation_error_if_password_does_not_contain_digits(self):
        self.assertRawPasswordValidationError(
            raw_password='password-without-digits',
            expected_message='Password must consist at least 1 number'
        )

    def test_should_raise_validation_error_if_password_does_not_contain_letters(self):
        self.assertRawPasswordValidationError(
            raw_password='1234567890',
            expected_message='Password must consist at least 1 letter'
        )
