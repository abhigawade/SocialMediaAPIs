from rest_framework import serializers
from .models import Follow

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.SerializerMethodField()
    followed = serializers.SerializerMethodField()
    class Meta:
        model = Follow
        fields = ['follower', 'followed']
        
    def get_follower(self, obj):
        return {
            'id': obj.follower.id,
            'email': obj.follower.email,
        }
        
    def get_followed(self, obj):
        return {
            'id': obj.followed.id,
            'email': obj.followed.email,
        }
        
class FollowingSerializer(serializers.ModelSerializer):
    followed = serializers.SerializerMethodField()

    class Meta:
        model = Follow
        fields = ['followed']

    def get_followed(self, obj):
        return {
            'id': obj.followed.id,
            'email': obj.followed.email,
        }
        
        
class FollowersSerializer(serializers.ModelSerializer):
    follower = serializers.SerializerMethodField()
    class Meta:
        model = Follow
        fields = ['follower']
        
    def get_follower(self, obj):
        return {
            'id': obj.follower.id,
            'email': obj.follower.email,
        }