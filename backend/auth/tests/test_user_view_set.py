from typing import List
from rest_framework.reverse import reverse
from auth.factories import UserFactory
from auth.models import User
from auth.views.user_view_set import UserSerializer
from main.tests import APITestCase


class TestUserViewSet(APITestCase):

    @classmethod
    def setUpTestData(cls):
        super(TestUserViewSet, cls).setUpTestData()
        cls.admin = UserFactory.create(is_admin=True)

    def setUp(self) -> None:
        super(TestUserViewSet, self).setUp()
        self.authenticate(user=self.admin)

    def tearDown(self) -> None:
        super(TestUserViewSet, self).tearDown()
        User.objects.all().delete()

    def test_should_return_list_of_all_users(self):
        users = UserFactory.create_batch(count=3)
        users.insert(0, self.admin)
        response = self.client.get(reverse('api:users-list'))
        self.assertEqual(response.status_code, 200)
        actual_response_data = response.json()
        self.assertIsInstance(actual_response_data, list)
        self.assertEqual(len(actual_response_data), len(users))
        expected_response_data = self._get_expected_list_response_data(users=users)
        self.assertEqual(actual_response_data, expected_response_data)

    @classmethod
    def _get_expected_list_response_data(cls, users: List[User]) -> List[dict]:
        expected_data = []
        for user in users:
            expected_data_item = cls._get_expected_detail_response_data(user=user)
            expected_data.append(expected_data_item)
        return expected_data

    @staticmethod
    def _get_expected_detail_response_data(user: User) -> dict:
        return {
            'id': user.pk,
            'name': user.name,
            'email': user.email,
            'username': user.username,
            'password': '**********' if user.password else '',
            'weekly_hours': user.weekly_hours,
            'is_active': user.is_active,
            'is_admin': user.is_admin
        }

    def test_should_create_user_and_return_it(self):
        request_data = {
            'name': 'Anna',
            'email': 'ana@examle.com',
            'username': 'ana',
            'password': 'pass4ana',
            'weekly_hours': 40,
        }
        next_user_id = UserFactory.next_id
        response = self.client.post(reverse('api:users-list'), json=request_data)
        self.assertEqual(response.status_code, 201)
        actual_response_data = response.json()
        expected_response_data = {
            'id': next_user_id,
            'name': 'Anna',
            'email': 'ana@examle.com',
            'username': 'ana',
            'password': '**********',
            'weekly_hours': 40.0,
            'is_active': True,  # default value
            'is_admin': False,  # default value
        }
        self.assertEqual(actual_response_data, expected_response_data)
        user = User.objects.get(pk=next_user_id)
        self.assertTrue(user.check_password(raw_password=UserSerializer.DEFAULT_RAW_PASSWORD))

    def test_should_return_single_user(self):
        user = UserFactory.create()
        response = self.client.get(reverse('api:users-detail', args=(user.pk,)))
        self.assertEqual(response.status_code, 200)
        actual_response_data = response.json()
        expected_response_data = self._get_expected_detail_response_data(user=user)
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_return_404_instead_of_the_user_when_user_does_not_exist(self):
        self.assertFalse(User.objects.filter(pk=UserFactory.next_id).exists())
        response = self.client.get(reverse('api:users-detail', args=(UserFactory.next_id,)))
        self.assertEqual(response.status_code, 404)
        actual_response_data = response.json()
        expected_response_data = {
            'detail': 'Not found.'
        }
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_update_user(self):
        user = UserFactory.create()
        request_data = {
            'name': f'{user.name}_updated',
            'email': f'updated_{user.email}',
            'username': user.username,
            'password': f'{UserSerializer.DEFAULT_RAW_PASSWORD}-updated',
            'weekly_hours': float(user.weekly_hours),
            'is_active': user.is_active,
            'is_admin': user.is_admin,
        }
        response = self.client.put(reverse('api:users-detail', args=(user.pk,)), json=request_data)
        self.assertEqual(response.status_code, 200)
        actual_response_data = response.json()
        expected_response_data = {
            'id': user.pk,
            **request_data,
            'password': '**********'
        }
        self.assertEqual(actual_response_data, expected_response_data)
        user.refresh_from_db()
        self.assertTrue(user.check_password(raw_password='pass4user!'))

    def test_should_not_update_user_when_all_required_fields_are_not_provided(self):
        user = UserFactory.create()
        request_data = {
            'name': user.name,
            'email': user.email,
            'username': user.username,
            # weekly_hours -> required field
        }
        response = self.client.put(reverse('api:users-detail', args=(user.pk,)), json=request_data)
        self.assertEqual(response.status_code, 400)
        actual_errors = response.json().get('errors')
        self.assertIsInstance(actual_errors, dict)
        expected_errors = {
            'weekly_hours': ['This field is required.'],
        }
        self.assertEqual(actual_errors, expected_errors)

    def test_should_partially_update_user(self):
        user = UserFactory.create()
        new_name = f'{user.name}_updated'
        request_data = {
            'name': new_name,
        }
        response = self.client.patch(reverse('api:users-detail', args=(user.pk,)), json=request_data)
        self.assertEqual(response.status_code, 200)
        actual_response_data = response.json()
        user.refresh_from_db()
        expected_response_data = self._get_expected_detail_response_data(user=user)
        expected_response_data['name'] = new_name
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_delete_user(self):
        user = UserFactory.create()
        response = self.client.delete(reverse('api:users-detail', args=(user.pk,)))
        self.assertEqual(response.status_code, 204)

    def test_should_return_404_instead_of_deleting_user_when_they_do_not_exist(self):
        response = self.client.delete(reverse('api:users-detail', args=(UserFactory.next_id,)))
        self.assertEqual(response.status_code, 404)
        actual_response_data = response.json()
        expected_response_data = {
            'detail': 'Not found.'
        }
        self.assertEqual(actual_response_data, expected_response_data)
