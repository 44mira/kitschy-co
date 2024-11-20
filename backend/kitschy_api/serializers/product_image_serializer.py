from rest_framework import serializers

from kitschy_api.models import ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
        extra_kwargs = {"product_id": {"write_only": True}}
