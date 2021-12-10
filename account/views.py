from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import RegistrationSerializer
from rest_framework.permissions import IsAuthenticated


class RegistrationAPIView(APIView):
    permission_classes = [~IsAuthenticated]

    def post(self, request):
        data = RegistrationSerializer(data=request.data)
        if not data.is_valid():
            return Response({
                "status": "fail",
                "data": data.errors
            })
        user = data.save()
        user.set_password(data.validated_data.get('password'))
        user.save()

        return Response({
            "status": "success"
        })
