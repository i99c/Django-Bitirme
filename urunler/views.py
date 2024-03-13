from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    kategoriler = Category.objects.all()

    return render(request,"index.html", {'kategoriler':kategoriler})

def abiye(request):
    
    abiye_urunler = Product.objects.filter(category__name='Abiye')

    return render(request, 'abiye.html', {'urunler': abiye_urunler})

def kadinAyakkabi(request):
    ayakkabi_urunler = Product.objects.filter(category__name='Kadın Ayakkabı')
    return render(request, "kayakkabi.html", {'urunler': ayakkabi_urunler})

def kozmetik(request):
    kozmetik_urunler = Product.objects.filter(category__name='Kozmetik')
    return render(request, "kozmetik.html", {'products': kozmetik_urunler})

def tamamlayici(request):

    tamamlayici_urunler = Product.objects.filter(category__name='Tamamlayıcı Ürünler (Kadın)')

    return render(request, "ktmmurun.html", {'products': tamamlayici_urunler})

def taki(request):
    taki_urunler = Product.objects.filter(category__name='Takı')
    return render(request, "taki.html", {'products': taki_urunler})

def gomlek(request):
    return render(request, "gomlek.html")

def takim(request):
    return render(request, "takim.html")

def ceket(request):
    return render(request, "ceket.html")

def yelek(request):
    return render(request, "yelek.html")

def eayakkabi(request):
    return render(request, "eayakkabi.html")

def etmmurun(request):
    return render(request, "etmmurun.html")

def anasayfa(request):
    return render(request, "index.html")

