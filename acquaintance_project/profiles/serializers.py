from rest_framework import serializers
from .models import Profile, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image', 'is_main', 'order']

class ProfileSerializer(serializers.ModelSerializer):
    main_photo_url = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id', 'first_name', 'last_name', 'gender', 'age', 'city',
            'interests', 'status', 'likes_count', 'main_photo_url', 'photos'
        ]

    def get_main_photo_url(self, obj):
        main = obj.photos.filter(is_main=True).first()
        return main.image.url if main else None
