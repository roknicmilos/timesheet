from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from auth.models import User
from main.serializers import SimpleSerializer
from auth.views.user_view_set import UserSerializer


class LoginSerializer(SimpleSerializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super(LoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = User.objects.filter(email=attrs['email']).first()
        if not (self.user and self.user.check_password(raw_password=attrs['password'])):
            raise serializers.ValidationError('Invalid credentials')

        return attrs

    def get_user(self) -> User:
        return self.user


class LoginAPIView(APIView):

    @staticmethod
    def post(request, **kwargs) -> Response:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user_serializer = UserSerializer(serializer.get_user())
            return Response(data=user_serializer.data, status=200)
        return Response(data={'errors': serializer.errors}, status=400)
