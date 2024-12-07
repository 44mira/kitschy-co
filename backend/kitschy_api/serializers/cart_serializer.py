from rest_framework import serializers

from kitschy_api.models import Cart


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
        items = Cart.objects.filter(cart_id=obj.cart_id)

        # check for empty
        if not items:
            return []

        instance = CartSerializer(items, many=True)

        return instance.data
