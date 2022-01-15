from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from main.utils import paginate_queryset
from projects.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientViewSet(viewsets.ViewSet):

    def list(self, request, **kwargs):
        clients = paginate_queryset(queryset=Client.objects.all(), request=request)
        serializer = ClientSerializer(clients, many=True)
        return Response(data=serializer.data)


    def create(self, request, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = Client.objects.create(**serializer.validated_data)
            serializer = ClientSerializer(client)
            return Response(data=serializer.data, status=201)
        return Response(data={'errors': serializer.errors}, status=400)

    @staticmethod
    def update(request, pk=None) -> Response:
        client = get_object_or_404(Client, pk=pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            client.update(**serializer.validated_data)
            serializer = ClientSerializer(client)
            return Response(data=serializer.data, status=200)
        return Response(data={'errors': serializer.errors}, status=400)

    @staticmethod
    def destroy(request, pk=None) -> Response:
        client = get_object_or_404(Client, pk=pk)
        client.delete()
        return Response(status=204)
