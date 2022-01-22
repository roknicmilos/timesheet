from rest_framework import serializers
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
