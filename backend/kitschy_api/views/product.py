from django.utils.timezone import now
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.schemas.coreapi import serializers


from kitschy_api.models import Product
from kitschy_api.serializers.product_serializer import (
    ProductImageSerializer,
    ProductSerializer,
)


class BatchedImageProductSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        fields = "__all__"

    images = inline_serializer(
        name="ProductImages",
        fields={
            "img_url": serializers.CharField(),
            "alt_desc": serializers.CharField(),
        },
        many=True,
    )


class ProductViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ["status"]
    
    @extend_schema(request=BatchedImageProductSerializer)
    def create(self, request):
        """
        The return json does not contain the `created_at` and `updated_at` \
        timestamps.
        You will have to get those from the `GET` queries.
        """

        images = request.data.pop("images")
        timestamp = now()

        request.data["created_at"] = timestamp
        request.data["updated_at"] = timestamp

        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        product_id = serializer.data["product_id"]  # pyright: ignore

        # create an image for each item
        for image in images:
            image["product"] = product_id
            img_serializer = ProductImageSerializer(data=image)
            img_serializer.is_valid(raise_exception=True)
            img_serializer.save()

        # create a dummy product as return value, does not set timestamps
        serializer = ProductSerializer(
            Product(product_id=product_id, **serializer.validated_data)
        )

        return Response(serializer.data)
