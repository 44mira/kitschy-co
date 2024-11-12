from django.urls import include, path
from kitschy_api.views import AddressViewSet
from kitschy_api.views.product import ProductViewSet
from kitschy_api.views.user import UserViewSet
from kitschy_api.views.order import OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"addresses", AddressViewSet)
router.register(r"products", ProductViewSet)
router.register(r"orders", OrderViewSet)
urlpatterns = [
    path("api/", include(router.urls)),
]
