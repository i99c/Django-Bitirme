from django.db import models

# Create your models here.
class Kategori(models.Model):
    ad = models.CharField(max_length=100)

class Urun(models.Model):
    ad = models.CharField(max_length=100)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    resim_url = models.URLField()
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    # Diğer özellikler