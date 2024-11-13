import uuid

from django.core.validators import MinValueValidator
from django.db import models

from .orders import Order
from .products import Product


class OrderItems(models.Model):
    items_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_items"
    )
    quantity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "order_items"
        unique_together = [
            "order_id",
            "product_id",
        ]  # Every product in an order should be unique
