from rest_framework import serializers

from kitschy_api.models import Order, OrderItems
from kitschy_api.serializers import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"

    def get_total(self, obj):
        items = self.get_items(obj)

        # check for empty
        if not items:
            return 0

        return sum(item["subtotal"] for item in items)

    def get_items(self, obj):
        items = OrderItems.objects.filter(order=obj.order_id)

        # check for empty
        if not items:
            return []

        instance = OrderItemSerializer(items, many=True)

        return instance.data
