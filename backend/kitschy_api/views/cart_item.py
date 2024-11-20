from rest_framework import mixins, viewsets

from kitschy_api.models import CartItem
from kitschy_api.serializers import CartItemSerializer


class CartItemViewSet(
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    """
    ViewSet for create, update, delete operations on order items.
    """

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
