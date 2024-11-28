from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from authentication.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [SearchFilter]
    search_fields = ['user__email']
    
    def update(self, request, *args, **kwargs):
        return Response({'message': 'You cannot update a post'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        post = Post.objects.get(id=post_id)
        if post.user == request.user:
            post.delete()
            return Response({'message': 'Post deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'You cannot delete all post'}, status=status.HTTP_400_BAD_REQUEST)
     
     
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response({'message': 'Post created successfully'}, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        
        if post_id:
            post = Post.objects.get(id=post_id, user=request.user)
            serializer = self.get_serializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            posts = Post.objects.filter(user=request.user)
            serializer = self.get_serializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)