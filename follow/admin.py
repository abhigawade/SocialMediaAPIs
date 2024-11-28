from django.contrib import admin
from .models import Follow
# Register your models here.
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed','created_at')
    list_filter = ('created_at',)
    search_fields = ('follower', 'followed')
    date_hierarchy = 'created_at'
    