from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from auth.models import User
from auth.utils import validate_raw_password
from main.serializers import SimpleSerializer


class PasswordSerializer(SimpleSerializer):
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError('Passwords do not match')

        validate_raw_password(raw_password=attrs['password'])

        return attrs


class PasswordChangeAPIView(APIView):

    @staticmethod
    def post(request, pk=None, **kwargs) -> Response:
        user = get_object_or_404(User, pk=pk)
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(raw_password=serializer.validated_data.get('password'))
            user.save()
            return Response(data={}, status=200)
        return Response(data={'errors': serializer.errors}, status=400)
