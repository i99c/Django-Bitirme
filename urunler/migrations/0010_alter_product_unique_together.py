# Generated by Django 5.0 on 2024-03-15 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0009_remove_product_product_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'category')},
        ),
    ]
