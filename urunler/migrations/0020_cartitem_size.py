# Generated by Django 5.0 on 2024-03-25 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0019_cart_cartitem_delete_sepetitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.CharField(default='XS', max_length=10),
        ),
    ]
