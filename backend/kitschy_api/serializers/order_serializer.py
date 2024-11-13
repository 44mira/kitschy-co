from rest_framework import serializers

from kitschy_api.models import Order, OrderItems
from kitschy_api.serializers import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"

    def get_total(self, obj):
        items = OrderItems.objects.filter(order_id=obj.order_id)
        if not items:
            return 0

        instance = OrderItemSerializer(items, many=True)

        return sum(item["subtotal"] for item in instance.data)
