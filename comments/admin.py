from django.contrib import admin
from .models import CommentsModel
# Register your models here.

@admin.register(CommentsModel)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id','post', 'user', 'content', 'created_at', 'updated_at')
    search_fields = ('post', 'user', 'content')
    readonly_fields= ('user', 'created_at', 'updated_at')
    
    def save_model(self, request, obj, form, change):
        """Set the current user as the comment's user."""
        if not change:
            obj.user = request.user
            return super().save_model(request, obj, form, change)
        
