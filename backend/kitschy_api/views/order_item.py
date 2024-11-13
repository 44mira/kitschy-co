from rest_framework import generics, mixins, viewsets

from kitschy_api.models import OrderItems
from kitschy_api.serializers.order_item_serializer import OrderItemSerializer


class OrderItemList(generics.ListAPIView):
    """
    Get the list of items associated to an order.
    """

    serializer_class = OrderItemSerializer

    def get_queryset(self):
        # Gets order_id from URL parameter
        order_id = self.kwargs.get("order_id")
        return OrderItems.objects.filter(order_id=order_id)


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
