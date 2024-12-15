from rest_framework import serializers

from kitschy_api.models import Product
from kitschy_api.serializers import ProductImageSerializer


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = "__all__"
