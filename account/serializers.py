from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'password', 'email']
        extra_kwargs = {
            'email': {
                'required': True
            }
        }
