from django.db import models
from authentication.models import User
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def likes_count(self):
        from likes.models import Likes
        return Likes.objects.filter(content_type=ContentType.objects.get_for_model(self), object_id=self.id).count()
    
    def __str__(self):
        return self.content