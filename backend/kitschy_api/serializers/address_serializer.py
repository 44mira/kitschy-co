from rest_framework import serializers
from kitschy_api.models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_id', 'user_id', 'region', 'city', 'postal_code', 'barangay', 'detailed_address']  # Explicit order of fields
        read_only_fields = ['address_id']
        

    def create(self, validated_data):
        return Address.objects.create(**validated_data)