from django.shortcuts import render
from .models import Follow
from authentication.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import FollowSerializer,FollowingSerializer,FollowersSerializer
# Create your views here.

class FollowUnfollowView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        followed_user_id = request.data.get('followed_user_id')
        followed_user = User.objects.get(id=followed_user_id)
        
        if followed_user == request.user:
            return Response({'message': 'You can not follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        
        existing_follow = Follow.objects.filter(followed=followed_user, follower=request.user)
        
        if existing_follow.exists():
            existing_follow.delete()
            return Response({'message': 'You are now Unfollowing this user'}, status=status.HTTP_200_OK)
        
        #Follow the user
        Follow.objects.create(follower=request.user, followed=followed_user)
        return Response({'message': 'You are now following this user'}, status=status.HTTP_200_OK)
    
    
class FollowersView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowersSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(followed=user)
    
    
class FollowingView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowingSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(follower=user)