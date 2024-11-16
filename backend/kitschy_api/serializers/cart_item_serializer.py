from rest_framework import serializers

from kitschy_api.models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    
    subtotal = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = "__all__"
    
    
    def get_subtotal(self,obj)->float:
        return obj.product.price * obj.quantity