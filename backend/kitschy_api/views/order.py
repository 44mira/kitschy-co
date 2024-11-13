from rest_framework import viewsets

from kitschy_api.models import Order
from kitschy_api.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
