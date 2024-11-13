from django.db import models
import uuid
from .users import User

class Cart(models.Model):
  cart_id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = "carts"
    ordering = ["-created_at"]
