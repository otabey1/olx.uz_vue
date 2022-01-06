from django.urls import path
from .views import RegistrationAPIView, LoginApiView, MeAPIView

app_name = 'account'

urlpatterns = [
    path('me/', MeAPIView.as_view(), name='me'),
    path('registration/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='user-login')
]
