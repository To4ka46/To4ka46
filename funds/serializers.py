from rest_framework import serializers
from .models import Collect, Payment

class PaymentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ["id", "collect", "user", "amount", "paid_at", "comment", "user_name"]
        read_only_fields = ["paid_at", "user"]

    def get_user_name(self, obj):
        user = obj.user
        return f"{user.first_name} {user.last_name}".strip() or user.username


class CollectSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    payments = PaymentSerializer(many=True, read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Collect
        fields = [
            "id", "author", "author_name", "title", "occasion", "description",
            "target_amount", "current_amount", "cover_image", "end_at",
            "created_at", "is_active", "payments"
        ]
        read_only_fields = ["author", "current_amount", "created_at", "is_active"]

    def get_author_name(self, obj):
        author = obj.author
        return f"{author.first_name} {author.last_name}".strip() or author.username
