# Generated by Django 5.1.3 on 2024-11-12 07:02

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('membership_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='First name can only contain letters, spaces, and hyphens', regex='^[^\\d]*$')])),
                ('last_name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Last name can only contain letters, spaces, and hyphens', regex='^[^\\d]*$')])),
                ('email', models.EmailField(max_length=255, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('password_hash', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number format: 09328910223/639328910223', regex='^\\+?(63|0)9\\d{9}$')])),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User')], default='USER', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
                'ordering': ['-created_at'],
            },
        ),
    ]
