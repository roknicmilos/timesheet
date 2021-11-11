from unittest import TestCase
from core.models import User


class UserTests(TestCase):

    def test_should_not_set_raw_password(self):
        password = 'password1234'
        user = User()
        user.set_password(raw_password=password)
        self.assertNotEqual(user.password, password)

    def test_should_return_false_when_password_is_incorrect(self):
        password = 'password1234'
        user = User()
        user.set_password(raw_password=password)
        is_correct_password = user.check_password(raw_password=f'incorrect{password}')
        self.assertFalse(is_correct_password)

    def test_should_return_true_when_password_is_correct(self):
        password = 'password1234'
        user = User()
        user.set_password(raw_password=password)
        is_correct_password = user.check_password(raw_password=password)
        self.assertTrue(is_correct_password)
