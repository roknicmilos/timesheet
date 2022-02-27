from typing import Type, List
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from main.models import BaseModel
from main.serializers import ListResponseSerializer
from rest_framework import serializers


class ViewSet(viewsets.ViewSet):
    model_class: Type[BaseModel]
    available_alphabet_letters_default_field: str = None
    serializer_class: Type[serializers.ModelSerializer]

    def list(self, request, **kwargs):
        serializer = ListResponseSerializer(
            model_class=self.model_class,
            model_serializer_class=self.serializer_class,
            request=request
        )
        return Response(data=serializer.data)

    @action(detail=False, methods=['get'], url_path=r'available-alphabet-letters')
    def available_alphabet_letters(self, request) -> Response:
        if not self.model_class:
            raise ImproperlyConfigured("ViewSet requires 'model_class' to be defined")

        if not self.available_alphabet_letters_default_field:
            raise ImproperlyConfigured("ViewSet requires 'available_alphabet_letters_default_field' to be defined")

        field_names = request.query_params.get('fields', self.available_alphabet_letters_default_field).split(',')

        data = {}
        for field_name in field_names:
            data[field_name] = self.model_class.objects.get_available_alphabet_letters(field_name=field_name)

        return Response(data=data)

    @classmethod
    def get_readonly_actions(cls) -> List[str]:
        return ['list', 'retrieve', 'available_alphabet_letters']
