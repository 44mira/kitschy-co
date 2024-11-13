from rest_framework import serializers
from kitschy_api.models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["cart_id", "user", "created_at", "updated_at"]
        read_only_fields = ["cart_id", "created_at", "updated_at"]
        