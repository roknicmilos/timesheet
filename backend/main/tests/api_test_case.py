from rest_framework.test import APITestCase as BaseAPITestCase
from rest_framework.authtoken.models import Token
from auth.models import User
from main.tests import CustomAPIClient


class APITestCase(BaseAPITestCase):
    client: CustomAPIClient
    client_class = CustomAPIClient

    def setUp(self) -> None:
        super(APITestCase, self).setUp()
        self.maxDiff = None

    def authenticate(self, user: User) -> None:
        token, _ = Token.objects.get_or_create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.key)
