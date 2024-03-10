# Generated by Django 5.0 on 2024-03-10 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
                ('resim_url', models.URLField()),
                ('fiyat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.kategori')),
            ],
        ),
    ]
