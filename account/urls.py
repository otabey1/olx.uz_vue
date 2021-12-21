from django.urls import path
from .views import RegistrationAPIView, LoginApiView

app_name = 'account'

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='user-login')
]
