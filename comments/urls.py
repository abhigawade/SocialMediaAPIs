from django.urls import path, include
from .views import CommentsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'comments', CommentsViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]