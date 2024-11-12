from django.urls import include, path
from kitschy_api.views.address import AddressViewSet
from kitschy_api.views.product import ProductViewSet
from kitschy_api.views.product_image import (
    ProductImageList,
    ProductImageViewSet,
)
from kitschy_api.views.user import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"addresses", AddressViewSet)
router.register(r"products", ProductViewSet)
router.register(r"products/image", ProductImageViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/products/images/<uuid:product_id>/", ProductImageList.as_view()),
]
