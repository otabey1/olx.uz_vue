from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=100, min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
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
            'password': {
                'required': True,
                'validators': [
                    MaxLengthValidator(100),
                    MinLengthValidator(6)
                ]
            },
        }


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=50, min_length=5,  required=True)
    password = serializers.CharField(max_length=100, min_length=0, required=True)


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'first_name', 'email', )


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'last_name', 'first_name', 'email']
