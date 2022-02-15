from rest_framework import serializers
from rest_framework.authtoken.models import Token
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

    @property
    def validated_data(self):
        from auth.serializers import UserSerializer
        data = UserSerializer(self.user).data
        token, _ = Token.objects.get_or_create(user=self.user)
        data['token'] = token.key
        return data
