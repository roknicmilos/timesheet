import json as json_utils
from rest_framework.test import APIClient


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
    def post(self, path: str, json: dict = None, **kwargs):
        return super(CustomAPIClient, self).post(path, **kwargs)

    @prepare_kwargs
    def put(self, path: str, json: dict = None, **kwargs):
        return super(CustomAPIClient, self).put(path, **kwargs)

    @prepare_kwargs
    def patch(self, path: str, json: dict = None, **kwargs):
        return super(CustomAPIClient, self).patch(path, **kwargs)
