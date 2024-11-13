from django.urls import include, path
from rest_framework.routers import DefaultRouter

from kitschy_api.views.address import AddressViewSet
from kitschy_api.views.cart import CartViewSet
from kitschy_api.views.order import OrderViewSet
from kitschy_api.views.order_item import OrderItemList, OrderItemViewSet
from kitschy_api.views.product import ProductViewSet
from kitschy_api.views.product_image import (
    ProductImageList,
    ProductImageViewSet,
)
from kitschy_api.views.user import UserViewSet

registered_viewsets = {
    "users": UserViewSet,
    "addresses": AddressViewSet,
    "orders": OrderViewSet,
    "order-item": OrderItemViewSet,
    "products": ProductViewSet,
    "products-image": ProductImageViewSet,
    "carts": CartViewSet,
}

router = DefaultRouter()
for viewset in registered_viewsets.items():
    router.register(*viewset)

urlpatterns = [
    path("", include(router.urls)),
    path("products/images/<uuid:product_id>/", ProductImageList.as_view()),
    path("orders/items/<uuid:order_id>/", OrderItemList.as_view()),
]
