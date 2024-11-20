from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from kitschy_api.models import Address, User

from .address_serializer import AddressSerializer


class UserRegisterSerializer(RegisterSerializer):
    username = None  # Remove username field
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    # Inherit the phone number validator from the model
    phone_number = serializers.CharField(
        max_length=20,
        required=True,
        validators=[
            User._meta.get_field("phone_number").validators[0]
        ],  # This gets the RegexValidator
    )

    address = AddressSerializer()

    def save(self, request):
        user = super().save(request)
        if self.validated_data:
            user.first_name = self.validated_data.get("first_name", "")
            user.last_name = self.validated_data.get("last_name", "")
            user.phone_number = self.validated_data.get("phone_number", "")
            user.save()

            # Create address using the nested serializer data
            address_data = self.validated_data.get("address", {})
            Address.objects.create(user=user, **address_data)

        return user

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "password1",
            "password2",
            "address",
        )


class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "membership_id",
            "addresses",
        )
