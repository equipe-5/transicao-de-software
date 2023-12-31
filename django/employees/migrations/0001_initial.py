# Generated by Django 4.2.7 on 2023-11-28 01:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(14)])),
                ('number_id', models.CharField(error_messages={'unique': 'Crachá já registrado'}, max_length=100, unique=True)),
                ('role', models.CharField(max_length=100)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addresses.address')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'ordering': ['-created_at'],
            },
        ),
    ]
