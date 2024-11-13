from rest_framework import viewsets

from kitschy_api.models import Product
from kitschy_api.serializers.product_serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
