# Generated by Django 5.1.3 on 2024-11-12 09:46

import uuid

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitschy_api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "product_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("desc", models.TextField()),
                (
                    "price",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0)
                        ]
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "products",
                "ordering": ["-product_id"],
            },
        ),
    ]
