from django.contrib import admin
from likes.models import Likes
# Register your models here.


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'content_object', 'created_at')
    search_fields = ('user', 'content_object')
    list_filter = ('created_at',)
