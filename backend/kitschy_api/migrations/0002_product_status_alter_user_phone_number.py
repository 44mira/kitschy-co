# Generated by Django 5.1.3 on 2024-11-25 14:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitschy_api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[
                    ("READY", "Ready for sale"),
                    ("ARCHIVED", "Hidden/archived"),
                ],
                default="READY",
            ),
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
