from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from auth.authentication import TokenAuthentication
from auth.models import User
from auth.permissions import IsAdmin
from auth.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

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
