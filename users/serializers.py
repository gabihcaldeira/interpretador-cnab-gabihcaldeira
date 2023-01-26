from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',
                  'first_name', 'last_name', 'is_active']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'is_active': {'read_only': True}
        }
