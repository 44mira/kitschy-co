import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    # Keep username but make it nullable since we're not using it
    username = models.CharField(
        max_length=150, null=True, blank=True, unique=True
    )

    email = models.EmailField(unique=True)
    membership_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+?(63|0)9\d{9}$",
                message="Enter a valid phone number format: 09328910223/639328910223",
            )
        ],
    )

    # Email based authentication
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):  # Fixed typo in method name
        return self.email
