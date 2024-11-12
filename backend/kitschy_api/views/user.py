from rest_framework import viewsets
from rest_framework.response import Response
from kitschy_api.models import User
from kitschy_api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer