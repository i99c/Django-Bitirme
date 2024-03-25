# Generated by Django 5.0 on 2024-03-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0012_favoriteitem_sepetitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sepet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urun_adi', models.CharField(max_length=255)),
                ('urun_fiyati', models.DecimalField(decimal_places=2, max_digits=10)),
                ('urun_resmi', models.CharField(max_length=255)),
                ('beden', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='sepetitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sepetitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='FavoriteItem',
        ),
        migrations.DeleteModel(
            name='SepetItem',
        ),
    ]