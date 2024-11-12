from kitschy_api.models import Order
from kitschy_api.serializers import OrderSerializer
from rest_framework import viewsets

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer