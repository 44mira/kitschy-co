from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from kitschy_api.models import Product
from kitschy_api.serializers.product_serializer import ProductSerializer


@extend_schema_view(
    list=extend_schema(description="Retrieves the list of **ALL** products")
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ["status"]
