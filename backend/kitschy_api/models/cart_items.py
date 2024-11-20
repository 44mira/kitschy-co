import uuid

from django.db import models

from .carts import Cart
from .products import Product


class CartItem(models.Model):
    item_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart_items"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cart_items"
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "cart_items"
        ordering = ["-item_id"]
