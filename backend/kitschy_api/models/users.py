from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.contrib.auth.hashers import make_password
import uuid


class User(models.Model):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    membership_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r"^[^\d]*$",
                message="First name can only contain letters, spaces, and hyphens",
            )
        ],
    )
    last_name = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r"^[^\d]*$",
                message="Last name can only contain letters, spaces, and hyphens",
            )
        ],
    )
    email = models.EmailField(
        max_length=255, unique=True, validators=[EmailValidator()]
    )
    password_hash = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+?(63|0)9\d{9}$",
                message="Enter a valid phone number format: 09328910223/639328910223",
            )
        ],
    )
    role = models.CharField(max_length=50, choices=Roles.choices, default=Roles.USER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def save(self, *args, **kwargs):
        if self._state.adding or not self.password_hash.startswith("pbkdf2_sha256"):
            self.password_hash = make_password(self.password_hash)
        super().save(*args, **kwargs)

