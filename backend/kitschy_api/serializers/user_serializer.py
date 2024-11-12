from rest_framework import serializers
from kitschy_api.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        exclude = ['password_hash']
        read_only_fields = ['user_id', 'membership_id', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['password_hash'] = validated_data.pop('password')
        return User.objects.create(**validated_data)