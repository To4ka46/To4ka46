from django.contrib import admin
from .models import Profile, Photo

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'age', 'city', 'status', 'likes_count']
    list_filter = ['gender', 'status', 'city']
    search_fields = ['user__username', 'user__email', 'city']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['profile', 'is_main', 'order', 'uploaded_at']
    list_filter = ['is_main']
