from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from auth.authentication import TokenAuthentication
from auth.permissions import IsReadingOrAdmin
from main.viewsets import ViewSet
from projects.models import Category
from projects.serializers import CategorySerializer


class CategoryViewSet(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReadingOrAdmin]
    model_class = Category
    serializer_class = CategorySerializer
    available_alphabet_letters_default_field = 'name'

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            category = self.model_class.objects.create(**serializer.validated_data)
            serializer = self.serializer_class(category)
            return Response(data=serializer.data, status=201)
        return Response(data={'errors': serializer.errors}, status=400)

    def update(self, request, pk=None) -> Response:
        category = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(category, data=request.data)
        if serializer.is_valid():
            category.update(**serializer.validated_data)
            serializer = self.serializer_class(category)
            return Response(data=serializer.data, status=200)
        return Response(data={'errors': serializer.errors}, status=400)

    def destroy(self, request, pk=None) -> Response:
        category = get_object_or_404(self.model_class, pk=pk)
        category.delete()
        return Response(status=204)
