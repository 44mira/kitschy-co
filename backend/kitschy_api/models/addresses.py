import uuid

from django.db import models

from .users import User


class Address(models.Model):
    address_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    # Foreign key to User
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="addresses"
    )
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    detailed_address = models.TextField()

    class Meta:
        db_table = "addresses"
        ordering = ["-address_id"]
