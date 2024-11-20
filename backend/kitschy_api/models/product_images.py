import uuid

from django.db import models

from .products import Product


class ProductImage(models.Model):
    product_image_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="products"
    )
    img_url = models.CharField(blank=False)
    alt_desc = models.TextField()

    class Meta:
        db_table = "product_images"
        ordering = ["-product_image_id"]
