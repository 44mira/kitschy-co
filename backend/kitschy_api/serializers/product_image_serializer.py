from rest_framework import serializers

from kitschy_api.models import ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product_image_id', 'img_url', 'alt_desc']
