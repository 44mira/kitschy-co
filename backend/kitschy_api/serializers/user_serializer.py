from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from kitschy_api.models import User

class UserRegisterSerializer(RegisterSerializer):
    username = None  # Remove username field
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'membership_id')