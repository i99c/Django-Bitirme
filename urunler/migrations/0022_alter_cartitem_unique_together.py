# Generated by Django 5.0 on 2024-03-25 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0021_alter_cartitem_size'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product', 'size')},
        ),
    ]