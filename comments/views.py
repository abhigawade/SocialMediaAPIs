from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from .models import CommentsModel
from post.models import Post
from .serializers import CommentsSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = CommentsModel.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_posts = Post.objects.filter(user=user)

        # Filter comments related to those posts
        return CommentsModel.objects.filter(post__in=user_posts)

    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.request.data.get('post_id')

        if not post_id:
            # If no post_id is provided, return a bad request response
            raise ValidationError("Post ID is required to create a comment.")

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise ValidationError("Post does not exist.")

        serializer.save(user=user, post=post)

    def partial_update(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user.id != self.request.user.id:
            return Response({'message': 'You are not allowed to edit this comment'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user.id != self.request.user.id:
            return Response({'message': 'You are not allowed to delete this comment'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
