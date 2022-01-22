from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from auth.authentication import TokenAuthentication
from auth.permissions import IsAdmin
from main.utils import paginate_queryset
from projects.models import Category
from projects.serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

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
