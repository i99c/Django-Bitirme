# Generated by Django 5.0 on 2024-03-15 10:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0005_remove_product_image_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
