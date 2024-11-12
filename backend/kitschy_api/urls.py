from django.urls import include, path
from kitschy_api.views.product import ProductViewSet
from kitschy_api.views.user import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
