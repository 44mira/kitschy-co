from rest_framework import viewsets
from kitschy_api.models import Cart
from kitschy_api.serializers import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
