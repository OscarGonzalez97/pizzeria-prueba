from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('token/basic/', ObtainAuthToken.as_view(), name='token_obtain_basic'),
    path('token/jwt/', TokenObtainPairView.as_view(), name='token_obtain_jwt'),
]
