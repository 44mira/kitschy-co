from rest_framework import serializers

from kitschy_api.models import Cart
from kitschy_api.serializers import CartItemSerializer


class CartSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            "cart_id",
            "user",
            "created_at",
            "updated_at",
            "total",
            "items",
        ]
        read_only_fields = ["cart_id", "created_at", "updated_at"]

    def get_total(self, obj):
        items = self.get_items(obj)

        # check for empty
        if not items:
            return 0

        return sum(item["subtotal"] for item in items)

    def get_items(self, obj):
        items = obj.cart_items.all()  # related_name='cart_items'
        if not items:
            return []

        return CartItemSerializer(items, many=True).data
