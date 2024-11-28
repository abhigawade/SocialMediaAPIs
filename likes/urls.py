from django.urls import path, include
from .views import LikeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'likes', LikeViewSet, basename='likes')

urlpatterns = [
    path('', include(router.urls)),
    
]