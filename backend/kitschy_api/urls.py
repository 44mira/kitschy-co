from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kitschy_api.views.user import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
urlpatterns = [
  path('api/', include(router.urls)),
]