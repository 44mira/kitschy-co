import uuid

from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    STATUS_CHOICES = {
        "READY": "Ready for sale",
        "ARCHIVED": "Hidden/archived",
    }

    product_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=255, blank=False)
    desc = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    quantity = models.IntegerField()  # Negative values mean pre-orders
    status = models.CharField(
        choices=STATUS_CHOICES,
        default="READY",
        null=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products"
        ordering = ["-product_id"]
