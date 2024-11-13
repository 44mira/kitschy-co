from rest_framework import generics, mixins, viewsets

from kitschy_api.models import OrderItems
from kitschy_api.serializers.order_item_serializer import OrderItemSerializer


class OrderItemList(generics.ListAPIView):
    """
    Get the list of items associated to an order.
    """

    queryset = OrderItems.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = "order_id"


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
