# Generated by Django 4.2.2 on 2023-11-14 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
