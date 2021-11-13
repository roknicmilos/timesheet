from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from core.factories.user import UserFactory


class UserViewSetTests(APITestCase):

    def test_should_return_list_of_all_users(self):
        users = UserFactory.create_batch(size=3)
        response = self.client.get(reverse('api:users'))
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), len(users))
        for item, user in zip(data, users):
            self.assertEqual(item.get('email'), user)
