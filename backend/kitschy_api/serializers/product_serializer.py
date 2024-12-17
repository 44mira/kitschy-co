from rest_framework import serializers

from kitschy_api.models import Product, ProductImage
from kitschy_api.serializers import ProductImageSerializer


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ["name", "desc", "price", "quantity", "status", "category", "images"]
    def create(self, validated_data):
        images_data = validated_data.pop('images', [])  # Remove images data and default to empty list
        product = Product.objects.create(**validated_data)
        
        # Handle any provided images
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)
            
        return product  