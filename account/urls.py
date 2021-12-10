from django.urls import path
from .views import RegistrationAPIView
app_name = 'account'

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='register')
]
