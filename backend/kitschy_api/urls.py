from django.urls import include, path
from rest_framework.routers import DefaultRouter

from kitschy_api.views.address import AddressViewSet
from kitschy_api.views.order import OrderViewSet
from kitschy_api.views.product import ProductViewSet
from kitschy_api.views.order_item import OrderItemList, OrderItemViewSet
from kitschy_api.views.product_image import (
    ProductImageList,
    ProductImageViewSet,
)
from kitschy_api.views.user import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"addresses", AddressViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"orders/items", OrderItemViewSet)
router.register(r"products", ProductViewSet)
router.register(r"products/image", ProductImageViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/products/images/<uuid:product_id>/", ProductImageList.as_view()),
]
