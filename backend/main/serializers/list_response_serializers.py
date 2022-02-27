import math
from typing import Type
from main.models import BaseModel
from main.serializers import SimpleSerializer
from main.utils import paginate_queryset
from rest_framework import serializers


class ListResponseSerializer(SimpleSerializer):

    def __init__(self, model_class: Type[BaseModel], model_serializer_class: Type[serializers.ModelSerializer],
                 request, *args, **kwargs):
        super(ListResponseSerializer, self).__init__(*args, **kwargs)
        self.model_class = model_class
        self.model_serializer_class = model_serializer_class
        self.request = request

    @property
    def data(self) -> dict:
        objects = paginate_queryset(queryset=self.model_class.objects.all(), request=self.request)
        model_serializer = self.model_serializer_class(objects, many=True)
        items = model_serializer.data
        total_items = self.model_class.objects.count()
        items_per_page = int(self.request.query_params.get('ipp', 50))
        pagination = {
            'total_items': total_items,
            'total_pages': math.ceil(total_items / items_per_page)
        }

        return {
            'items': items,
            'pagination': pagination
        }
