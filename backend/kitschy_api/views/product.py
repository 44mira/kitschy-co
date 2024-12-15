from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import mixins, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
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
            "img_url": serializers.FileField(),
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
    filterset_fields = ["status", "category", "creators"]
    parser_classes = (
        MultiPartParser,
        FormParser,
    )  # Add parsers for file upload

    @extend_schema(request=BatchedImageProductSerializer)
    def create(self, request):
        """
        The return json does not contain the `created_at` and `updated_at` \
        timestamps.
        You will have to get those from the `GET` queries.
        """
        # Get the images files and descriptions
        images = request.FILES.getlist("images", [])
        alt_descs = request.data.getlist("alt_descs", [])

        # Create the product first
        product_data = {
            "name": request.data.get("name"),
            "desc": request.data.get("desc"),
            "price": request.data.get("price"),
            "quantity": request.data.get("quantity"),
            "status": request.data.get("status"),
            "category": request.data.get("category"),
            "creators": request.data.getlist("creators", []),
        }

        serializer = ProductSerializer(data=product_data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        # Create images
        for i, image in enumerate(images):
            alt_desc = alt_descs[i] if i < len(alt_descs) else ""
            image_data = {
                "product": product.product_id,
                "img_url": image,
                "alt_desc": alt_desc,
            }
            img_serializer = ProductImageSerializer(data=image_data)
            img_serializer.is_valid(raise_exception=True)
            img_serializer.save()

        # Return the complete product with images
        return Response(ProductSerializer(product).data)
