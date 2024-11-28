from rest_framework import serializers
from .models import Post
from authentication.models import User

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'user', 'content','likes_count', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {'user': {'read_only': True}}
        
    def get_likes_count(self, obj):
        # Safely retrieve request from context
        request = self.context.get('request', None)
        if request and request.method == 'GET':
            return obj.likes_count
        return 0