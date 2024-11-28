from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created_at', 'updated_at')
    search_fields = ('user', 'content')