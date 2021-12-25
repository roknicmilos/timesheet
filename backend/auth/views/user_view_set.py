from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from auth.models import User
from main.utils import mask_string


class UserSerializer(serializers.ModelSerializer):
    DEFAULT_RAW_PASSWORD = 'pass4user!'

    class Meta:
        model = User
        fields = [
            'id', 'email', 'is_active', 'is_admin', 'name', 'password', 'username', 'weekly_hours',
        ]
        extra_kwargs = {
            'password': {'required': False},
            'weekly_hours': {'required': True},
        }

    def to_representation(self, instance):
        kwargs = super(UserSerializer, self).to_representation(instance=instance)
        masked_password = mask_string(kwargs['password'])
        kwargs['password'] = masked_password[:10] if len(masked_password) > 10 else masked_password
        return kwargs

    def to_internal_value(self, data):
        values = super(UserSerializer, self).to_internal_value(data=data)
        values['password'] = self.DEFAULT_RAW_PASSWORD
        return values


class UserViewSet(viewsets.ViewSet):

    @staticmethod
    def list(request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data)

    @staticmethod
    def create(request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            serializer = UserSerializer(user)
            return Response(data=serializer.data, status=201)
        return Response(data={'errors': serializer.errors}, status=400)

    @staticmethod
    def retrieve(request, pk=None) -> Response:
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(data=serializer.data)

    @staticmethod
    def update(request, pk=None) -> Response:
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            user.update(**serializer.validated_data)
            serializer = UserSerializer(user)
            return Response(data=serializer.data, status=200)
        return Response(data={'errors': serializer.errors}, status=400)

    @staticmethod
    def partial_update(request, pk=None) -> Response:
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user.update(**serializer.validated_data)
            serializer = UserSerializer(user)
            return Response(data=serializer.data, status=200)
        return Response(data={'errors': serializer.errors}, status=400)

    @staticmethod
    def destroy(request, pk=None) -> Response:
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=204)
