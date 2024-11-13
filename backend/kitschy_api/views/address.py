from rest_framework import viewsets

from kitschy_api.models import Address
from kitschy_api.serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
