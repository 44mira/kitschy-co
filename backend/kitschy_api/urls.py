from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kitschy_api.views.user import UserViewSet
from kitschy_api.views.product import ProductViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"products", ProductViewSet)
urlpatterns = [
    path("api/", include(router.urls)),
]
