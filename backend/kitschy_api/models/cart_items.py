from django.db import models
import uuid
from .carts import Cart
from .products import Product
class CartItems(models.Model):
  items_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  cart =  models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
  product =  models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
  price = models.DecimalField(max_digits=10, decimal_places=2)

  class Meta:
    db_table = "cart_items"
    ordering = ["-items_id"]