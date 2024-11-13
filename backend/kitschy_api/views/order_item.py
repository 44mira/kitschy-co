from rest_framework import mixins, viewsets

from kitschy_api.models import OrderItems
from kitschy_api.serializers.order_item_serializer import OrderItemSerializer


class OrderItemViewSet(
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    """
    ViewSet for create, update, delete operations on order items.
    """

    queryset = OrderItems.objects.all()
    serializer_class = OrderItemSerializer
