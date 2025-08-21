from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, MeView

urlpatterns = [
    path("auth/register/", RegisterView.as_view()),
    path("auth/login/", TokenObtainPairView.as_view(), name="jwt_login"),  
    path("auth/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
     path("auth/me/", MeView.as_view(), name="me"),
]
