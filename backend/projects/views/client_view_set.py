from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from auth.authentication import TokenAuthentication
from auth.permissions import IsAdmin
from main.utils import paginate_queryset
from main.viewsets import ViewSet
from projects.models import Client
from projects.serializers import ClientSerializer


class ClientViewSet(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]
    model_class = Client
    available_alphabet_letters_default_field = 'name'

    def list(self, request, **kwargs):
        clients = paginate_queryset(queryset=self.model_class.objects.all(), request=request)
        serializer = ClientSerializer(clients, many=True)
        return Response(data=serializer.data)


    def create(self, request, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = self.model_class.objects.create(**serializer.validated_data)
            serializer = ClientSerializer(client)
            return Response(data=serializer.data, status=201)
        return Response(data={'errors': serializer.errors}, status=400)

    def update(self, request, pk=None) -> Response:
        client = get_object_or_404(self.model_class, pk=pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            client.update(**serializer.validated_data)
            serializer = ClientSerializer(client)
            return Response(data=serializer.data)
        return Response(data={'errors': serializer.errors}, status=400)

    def destroy(self, request, pk=None) -> Response:
        client = get_object_or_404(self.model_class, pk=pk)
        client.delete()
        return Response(status=204)
