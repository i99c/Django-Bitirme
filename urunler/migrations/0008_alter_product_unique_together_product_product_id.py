# Generated by Django 5.0 on 2024-03-15 13:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0007_alter_product_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
