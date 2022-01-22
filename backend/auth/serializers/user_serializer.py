from rest_framework import serializers
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
