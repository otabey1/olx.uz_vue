from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer, LoginSerializers, ProfileSerializers, MeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


class MeAPIView(APIView):
    def get(self, request):
        print(1)
        return Response({
            "status": "success",
            'data': MeSerializer(request.user).data
        })


class RegistrationAPIView(CreateAPIView):
    permission_classes = [~IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "status": "fail",
                "data": serializer.errors
                })
        serializer.save()
        return Response({
            "status": "success"
        })


class LoginApiView(APIView):
    permission_classes = [~IsAuthenticated]

    def post(self, request):
        serializers = LoginSerializers(data=request.data)
        if not serializers.is_valid():
            Response({"status": "fail", "data": serializers.errors})

        user = authenticate(request, **serializers.validated_data)
        if user is None:
            return Response({
                "status": "fail",
                "data": "Login va/yoki parol noto'g'ri"
            })

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "status": "success",
            "data": {
                "user": ProfileSerializers(user).data,
                "token": token.key
            }
        })
