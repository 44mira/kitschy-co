import uuid

from django.core.validators import MinValueValidator
from django.db import models

from kitschy_api.models.users import User


class Product(models.Model):
    STATUS_CHOICES = {
        "READY": "Ready for sale",
        "ARCHIVED": "Hidden/archived",
    }

    CATEGORY_CHOICES = {
        "MERCH": "Merchandise",
        "PRINT": "Misbeeks' Printing",
        "CAFE": "Cafe and Pastries",
        "MINIMART": "Mini-mart",
        "WORKSHOP": "Workshop",
    }

    product_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=255, blank=False)
    desc = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    quantity = models.IntegerField(
        default=0
    )  # Negative values mean pre-orders
    status = models.CharField(
        choices=STATUS_CHOICES,
        default="READY",
        null=False,
    )
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        default="MERCH",
        null=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creators = models.ManyToManyField(User, related_name="users")

    class Meta:
        db_table = "products"
        ordering = ["-product_id"]
