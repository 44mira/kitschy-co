from kitschy_api.models import Product
from kitschy_api.serializers.product_serializer import ProductSerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
