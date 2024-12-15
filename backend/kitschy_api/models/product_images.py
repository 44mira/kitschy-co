import uuid

from django.db import models

from .products import Product


class ProductImage(models.Model):
    def get_s3_path(instance, filename):
        return f"product_images/{filename}"

    product_image_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="products"
    )
    image = models.FileField(upload_to=get_s3_path, null=True, blank=False)
    alt_desc = models.TextField()

    class Meta:
        db_table = "product_images"
        ordering = ["-product_image_id"]
