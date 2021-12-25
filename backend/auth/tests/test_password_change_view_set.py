from rest_framework.reverse import reverse
from auth.models import User
from auth.factories import UserFactory
from main.tests.mixins import APITestCase


class TestPasswordChangeViewSet(APITestCase):

    def tearDown(self) -> None:
        super(TestPasswordChangeViewSet, self).tearDown()
        User.objects.all().delete()

    def test_should_change_user_password(self):
        user = UserFactory.create()
        raw_password = 'pass4thisUSER!'
        user.set_password(raw_password)
        user.save()
        new_password = f'{raw_password}-updated'
        request_data = {
            'password': new_password,
            'password_confirm': new_password,
        }
        self.assertFalse(user.check_password(raw_password=new_password))
        response = self.client.post(reverse('api:password-change', args=(user.pk,)), json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {})
        user.refresh_from_db()
        self.assertTrue(user.check_password(raw_password=new_password))

    def test_should_return_404_instead_of_changing_the_password_when_user_does_not_exist(self):
        response = self.client.post(reverse('api:password-change', args=(UserFactory.next_id,)))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {
            'detail': 'Not found.'
        })

    def test_should_return_400_when_password_and_password_confirm_do_not_match(self):
        user = UserFactory.create()
        request_data = {
            'password': 'new-pass-4-user',
            'password_confirm': 'new-pass-4-user-but-different',
        }
        response = self.client.post(reverse('api:password-change', args=(user.pk,)), json=request_data)
        self.assertEqual(response.status_code, 400)
        actual_response_data = response.json()
        expected_response_data = {
            'errors': {
                'non_field_errors': ['Passwords do not match'],
            }
        }
        self.assertEqual(actual_response_data, expected_response_data)
