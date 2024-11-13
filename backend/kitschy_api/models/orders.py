import uuid

from django.db import models

from .users import User


class Order(models.Model):
    order_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders"
    )
    method = models.CharField(max_length=50)
    status = models.CharField(max_length=50, null=False)
    delivery_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "orders"
        ordering = ["-created_at"]
