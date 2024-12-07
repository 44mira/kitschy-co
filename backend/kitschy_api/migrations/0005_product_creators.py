# Generated by Django 5.1.3 on 2024-11-25 19:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitschy_api", "0004_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="creators",
            field=models.ManyToManyField(
                related_name="users", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
