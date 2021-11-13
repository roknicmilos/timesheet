import json as json_utils
from rest_framework.test import APIClient, APITestCase as BaseAPITestCase


class CustomAPIClient(APIClient):

    @staticmethod
    def prepare_kwargs(func):
        def wrapper(*args, json=None, **kwargs):
            if json:
                kwargs['data'] = json_utils.dumps(json)
                kwargs['content_type'] = 'application/json'
            return func(*args, **kwargs)

        return wrapper

    @prepare_kwargs
    def post(self, *args, json: dict = None, **kwargs):
        return super(CustomAPIClient, self).post(*args, **kwargs)

    @prepare_kwargs
    def put(self, *args, json: dict = None, **kwargs):
        return super(CustomAPIClient, self).put(*args, **kwargs)

    @prepare_kwargs
    def patch(self, *args, json: dict = None, **kwargs):
        return super(CustomAPIClient, self).patch(*args, **kwargs)


class APITestCase(BaseAPITestCase):
    client: CustomAPIClient
    client_class = CustomAPIClient
