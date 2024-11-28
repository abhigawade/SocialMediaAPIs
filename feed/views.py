from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import Post
from follow.models import Follow
from post.serializers import PostSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class FeedView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        user = request.user
        
        followed_users = Follow.objects.filter(follower=user).values_list('followed', flat=True)
        followed_posts = Post.objects.filter(user__in=followed_users) 
        
        serializer = PostSerializer(followed_posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)