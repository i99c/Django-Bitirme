# Generated by Django 5.0 on 2024-03-25 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0013_sepet_remove_sepetitem_product_remove_sepetitem_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sepet',
        ),
    ]
