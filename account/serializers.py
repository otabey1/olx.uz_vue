from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=100, min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'password', 'email']
        extra_kwargs = {
            'username': {
                'required': True,
                'validators': [
                    MaxLengthValidator(50),
                    MinLengthValidator(5)
                ]
            },
            'email': {
                'required': True,
                'validators': [
                    MaxLengthValidator(200)
                ]
            }
        }


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=50, min_length=5,  required=True)
    password = serializers.CharField(max_length=100, min_length=0, required=True)


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'last_name', 'first_name', 'email']
