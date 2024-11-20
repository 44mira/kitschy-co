from rest_framework import mixins, viewsets

from kitschy_api.models import ProductImage
from kitschy_api.serializers.product_image_serializer import (
    ProductImageSerializer,
)


class ProductImageViewSet(
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
