# serializers/user_serializer.py
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from kitschy_api.models import Address, User

from .address_serializer import (  # Import the existing serializer
    AddressSerializer,
)


class UserRegisterSerializer(RegisterSerializer):
    username = None  # Remove username field
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    # TODO: Have address fields in register serializer
    """ # Address fields
    region = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    postal_code = serializers.CharField(required=True)
    barangay = serializers.CharField(required=True)
    detailed_address = serializers.CharField(required=True) """

    def save(self, request):
        user = super().save(request)
        if self.validated_data:
            user.first_name = self.validated_data.get("first_name", "")
            user.last_name = self.validated_data.get("last_name", "")
            user.phone_number = self.validated_data.get("phone_number", "")
            user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "membership_id",
            # "addresses", TODO: link the address serializer here
        )
