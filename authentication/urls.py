from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'register', UserRegistrationView, basename='register')

router.register(r'login', UserLoginView, basename='login')

urlpatterns = [
    path('', include(router.urls)),
     path('profile/', UserProfileView.as_view({'get': 'retrieve','put': 'update'}), name='profile'),
     path('change-password/', UserChangePasswordView.as_view({'put': 'update'}), name='change-password'),
]