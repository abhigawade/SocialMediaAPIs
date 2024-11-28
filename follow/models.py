from django.db import models
from authentication.models import User
# Create your models here.

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)  # follower is the user who is following / current user
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)  # followed is the user who is being followed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('follower', 'followed')  # Ensure a user can follow another user only once

    def __str__(self):
        return f"{self.follower} follows {self.followed}"