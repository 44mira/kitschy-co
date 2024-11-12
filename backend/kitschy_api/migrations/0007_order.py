# Generated by Django 5.1.3 on 2024-11-12 18:02

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitschy_api", "0006_alter_address_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "order_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("method", models.CharField(max_length=50)),
                ("status", models.CharField(max_length=50)),
                ("delivery_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="kitschy_api.user",
                    ),
                ),
            ],
            options={
                "db_table": "orders",
                "ordering": ["-created_at"],
            },
        ),
    ]
