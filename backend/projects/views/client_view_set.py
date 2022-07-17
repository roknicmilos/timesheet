from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as filters
from auth.authentication import TokenAuthentication
from auth.permissions import IsReadingOrAdmin
from main.viewsets import ViewSet
from projects.filters import ClientFilter
from projects.models import Client
from projects.serializers import ClientSerializer


class ClientViewSet(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReadingOrAdmin]
    model_class = Client
    serializer_class = ClientSerializer
    available_alphabet_letters_default_field = 'name'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ClientFilter

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            client = self.model_class.objects.create(**serializer.validated_data)
            serializer = self.serializer_class(client)
            return Response(data=serializer.data, status=201)
        return Response(data={'errors': serializer.errors}, status=400)

    def update(self, request, pk=None) -> Response:
        client = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(client, data=request.data)
        if serializer.is_valid():
            client.update(**serializer.validated_data)
            serializer = self.serializer_class(client)
            return Response(data=serializer.data)
        return Response(data={'errors': serializer.errors}, status=400)

    def destroy(self, request, pk=None) -> Response:
        client = get_object_or_404(self.model_class, pk=pk)
        client.delete()
        return Response(status=204)
