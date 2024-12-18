from django.db import models
from authentication.models import User
from post.models import Post
from comments.models import CommentsModel
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)
    
    unique_together = (('user', 'content_type', 'object_id'),)
    
    def __str__(self):
        return f"{self.user} liked {self.content_object}"