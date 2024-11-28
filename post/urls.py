from django.urls import path, include
from .views import PostViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'posts', PostViewset, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    
]