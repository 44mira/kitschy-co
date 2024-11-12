from kitschy_api.models import ProductImage
from kitschy_api.serializers.product_image_serializer import (
    ProductImageSerializer,
)
from rest_framework import viewsets


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
