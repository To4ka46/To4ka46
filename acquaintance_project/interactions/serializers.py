from rest_framework import serializers
from .models import Interaction, ViewedProfile, Match

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['id', 'user', 'target_profile', 'action', 'created_at']

class ViewedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewedProfile
        fields = ['profile', 'viewed_at']

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['user1', 'user2', 'created_at']
