from rest_framework import serializers

from kitschy_api.models import Product, ProductImage
from kitschy_api.serializers import ProductImageSerializer


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_images(self, obj):
        images = ProductImage.objects.filter(product=obj.product_id)

        if not images:
            return []

        instance = ProductImageSerializer(images, many=True)

        return instance.data

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)
        # Remove keys with null values
        return {
            key: value
            for key, value in representation.items()
            if value is not None
        }
