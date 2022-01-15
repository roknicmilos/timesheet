from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from main.utils import paginate_queryset
from projects.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryViewSet(viewsets.ViewSet):

    def list(self, request, **kwargs):
        categories = paginate_queryset(queryset=Category.objects.all(), request=request)
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)


    def create(self, request, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = Category.objects.create(**serializer.validated_data)
            serializer = CategorySerializer(category)
            return Response(data=serializer.data, status=201)
        return Response(data={'errors': serializer.errors}, status=400)

    @staticmethod
    def update(request, pk=None) -> Response:
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            category.update(**serializer.validated_data)
            serializer = CategorySerializer(category)
            return Response(data=serializer.data, status=200)
        return Response(data={'errors': serializer.errors}, status=400)

    @staticmethod
    def destroy(request, pk=None) -> Response:
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=204)
