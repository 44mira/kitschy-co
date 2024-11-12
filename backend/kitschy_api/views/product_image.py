from kitschy_api.models import ProductImage
from kitschy_api.serializers.product_image_serializer import (
    ProductImageSerializer,
)
from rest_framework import generics, mixins, viewsets


class ProductImageList(generics.ListAPIView):
    """
    Get the list of images associated to a `product`.
    """

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    lookup_field = "product_id"


class ProductImageViewSet(
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
