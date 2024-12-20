import uuid

from django.db import models

from .users import User


class Order(models.Model):
    METHOD_CHOICES = {
        "COD": "Cash on Delivery",
        "ONLINE": "Online Payment",
    }

    STATUS_CHOICES = {
        "PENDING": "Pending",
        "PROCESSING": "Processing",
        "DELIVERED": "Delivered",
        "CANCELLED": "Cancelled",
    }

    order_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    method = models.CharField(
        max_length=50,
        choices=METHOD_CHOICES,
        default="COD",
    )
    status = models.CharField(
        max_length=50, null=False, choices=STATUS_CHOICES, default="Pending"
    )
    delivery_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "orders"
        ordering = ["-created_at"]
