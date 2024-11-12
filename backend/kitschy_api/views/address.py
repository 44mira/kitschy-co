from kitschy_api.models import Address
from kitschy_api.serializers import AddressSerializer
from rest_framework import viewsets


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
