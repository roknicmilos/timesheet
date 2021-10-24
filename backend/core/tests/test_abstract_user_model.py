from unittest import TestCase

from core.models.abstract_user import AbstractUser


class AbstractUserModelTests(TestCase):

    def test_should_not_be_able_to_instantiate_abstract_user(self):
        try:
            AbstractUser()
        except Exception as e:
            self.assertEqual(str(e), f'{AbstractUser.__name__} cannot be instantiated')
        else:
            self.fail('Did not raise Exception')
