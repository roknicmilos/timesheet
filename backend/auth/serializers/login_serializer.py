from rest_framework import serializers
from auth.models import User
from main.serializers import SimpleSerializer


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
