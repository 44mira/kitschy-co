from django.db import models
import uuid
from .orders import Order

class OrderItems(models.Model):
    items_id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    #product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  

    class Meta:
        db_table = 'order_items'