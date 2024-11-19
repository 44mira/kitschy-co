# kitschy_api/models.py
import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    email = models.EmailField(unique=True)
    membership_id = models.UUIDField(
        null=True,  # Allow null
        blank=True,  # Allow blank in forms
        unique=True,  # Keep unique constraint
        editable=True,
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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()  # type: ignore

    def __str__(self):
        return self.email
