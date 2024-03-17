# Generated by Django 5.0 on 2024-03-15 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0006_product_product_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'category', 'price')},
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
    ]