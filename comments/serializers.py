from .models import CommentsModel
from rest_framework import serializers
from authentication.models import User
from post.models import Post

class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()

    class Meta:
        model = CommentsModel
        fields = ('id', 'user', 'post', 'content', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
        
    def get_user(self, obj):
        return obj.user.id
    
    def get_post(self, obj):
        return obj.post.id
    
    # def create(self, validated_data):
    #     post = Post.objects.get(id=validated_data.pop('post'))
    #     if post is None:
    #         raise serializers.ValidationError('Post is required')
    #     return super().create(validated_data)