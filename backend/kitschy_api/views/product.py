from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from kitschy_api.models import Product
from kitschy_api.serializers.product_serializer import ProductSerializer


@extend_schema_view(
    list=extend_schema(description="Retrieves the list of **ALL** products")
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False)
    def ready(self):
        """
        Retrieves the list of **READY** products
        """
        ready_products = Product.objects.filter(status="READY")

        serializer = self.get_serializer(ready_products, many=True)
        return Response(serializer.data)
