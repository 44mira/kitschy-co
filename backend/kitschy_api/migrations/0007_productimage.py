# Generated by Django 5.1.3 on 2024-11-12 18:04

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitschy_api", "0006_alter_address_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "product_image_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("img_url", models.CharField()),
                ("alt_desc", models.TextField()),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="kitschy_api.product",
                    ),
                ),
            ],
            options={
                "db_table": "product_images",
                "ordering": ["-product_image_id"],
            },
        ),
    ]
