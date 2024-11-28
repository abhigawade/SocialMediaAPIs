from rest_framework import serializers
from likes.models import Likes

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['user', 'content_type', 'object_id', 'created_at']
        read_only_fields = ['created_at']
        
        def create(self, validated_data):
            user = validated_data.get('user')
            content_type = validated_data.get('content_type')
            object_id = validated_data.get('object_id')
            
            like, created = Likes.objects.get_or_create(user=user, content_type=content_type, object_id=object_id)
            if not created:
                like.delete()
            return like