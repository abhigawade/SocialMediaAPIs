from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from likes.models import Likes
from likes.serializers import LikesSerializer
from authentication.models import User
from post.models import Post
from comments.models import CommentsModel
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
# Create your views here.

class LikeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        user = request.user
        content_type_str = request.data.get('content_type')
        object_id = request.data.get('object_id')
        
        if content_type_str not in ['post', 'commentsmodel']:
            return Response({'error': 'Invalid content type'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Convert string to ContentType instance
        content_type = ContentType.objects.get(model=content_type_str)
        
        
        if content_type == 'post':
            content_object = get_object_or_404(Post, id=object_id)
        elif content_type == 'comment':
            content_object = get_object_or_404(CommentsModel, id=object_id)
            
        like = Likes.objects.filter(user=user, content_type_id=content_type.id, object_id=object_id)
        
        if like.exists():
            like.delete()
            return Response({'message': 'Like deleted successfully'}, status=status.HTTP_200_OK)
        else:
            like = Likes.objects.create(user=user, content_type=content_type, object_id=object_id)
            return Response({'message': 'Like created successfully'}, status=status.HTTP_201_CREATED)
    