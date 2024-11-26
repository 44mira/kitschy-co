# Generated by Django 5.1.3 on 2024-11-26 02:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitschy_api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="quantity",
            new_name="stock",
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                max_length=20,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Enter a valid phone number format:09328910223/639328910223",
                        regex="^\\+?(63|0)9\\d{9}$",
                    )
                ],
            ),
        ),
    ]
