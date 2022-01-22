from rest_framework.reverse import reverse
from auth.models import User
from auth.factories import UserFactory
from main.tests import APITestCase


class TestPasswordChangeViewSet(APITestCase):
    user: User
    raw_password: str

    @classmethod
    def setUpTestData(cls):
        super(TestPasswordChangeViewSet, cls).setUpTestData()
        cls.user = UserFactory.create()
        cls.raw_password = 'pass4thisUSER!'
        cls.user.set_password(cls.raw_password)
        cls.user.save()

    def setUp(self) -> None:
        super(TestPasswordChangeViewSet, self).setUp()
        self.authenticate(user=self.user)


    def tearDown(self) -> None:
        super(TestPasswordChangeViewSet, self).tearDown()
        User.objects.all().delete()

    def test_should_change_user_password(self):
        new_password = f'{self.raw_password}-updated'
        request_data = {
            'password': new_password,
            'password_confirm': new_password,
        }
        self.assertFalse(self.user.check_password(raw_password=new_password))
        response = self.client.post(
            path=reverse('api:password-change', args=(self.user.pk,)),
            data=request_data,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {})
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password(raw_password=new_password))

    def test_should_return_400_when_password_and_password_confirm_do_not_match(self):
        request_data = {
            'password': 'new-pass-4-user',
            'password_confirm': 'new-pass-4-user-but-different',
        }
        response = self.client.post(reverse('api:password-change', args=(self.user.pk,)), json=request_data)
        self.assertEqual(response.status_code, 400)
        actual_response_data = response.json()
        expected_response_data = {
            'errors': {
                'non_field_errors': ['Passwords do not match'],
            }
        }
        self.assertEqual(actual_response_data, expected_response_data)
