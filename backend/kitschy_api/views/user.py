from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from kitschy_api.models import User
from kitschy_api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]