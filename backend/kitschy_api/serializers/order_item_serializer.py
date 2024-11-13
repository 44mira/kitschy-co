from rest_framework import serializers
from kitschy_api.models import OrderItems

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_id.name', read_only=True)
    product_price = serializers.DecimalField(
        source='product_id.price',
        max_digits=10, 
        decimal_places=2, 
        read_only=True
    )
    # This tells DRF to look for a method called get_subtotal() in this serializer
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = OrderItems
        fields = [
            "items_id",
            "order_id",
            "product_id",
            "product_name",
            "product_price",
            "quantity",
            "subtotal",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["items_id"]
    def get_subtotal(self, obj)->float:  # obj is the OrderItems instance
        return obj.product_id.price * obj.quantity