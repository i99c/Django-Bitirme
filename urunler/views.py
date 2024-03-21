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
    return render(request, "kayakkabi.html", {'ayakkabilar': ayakkabi_urunler})

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

    gomlek_urunler = Product.objects.filter(category__name='Gömlek')

    return render(request, "gomlek.html", {'erkekurunler': gomlek_urunler})

def takim(request):

    takim_urunler = Product.objects.filter(category__name='Takım')

    return render(request, "takim.html",{'erkekurunler': takim_urunler})

def ceket(request):

    ceket_urunler = Product.objects.filter(category__name='Ceket')

    return render(request, "ceket.html",{'erkekurunler': ceket_urunler})

def yelek(request):

    yelek_urunler = Product.objects.filter(category__name='Yelek')

    return render(request, "yelek.html",{'erkekurunler':yelek_urunler})

def eayakkabi(request):

    eayakkabi_urunler = Product.objects.filter(category__name='Erkek Ayakkabı')

    return render(request, "eayakkabi.html",{'eayakkabilar':eayakkabi_urunler})

def etmmurun(request):

    etamamlayici_urunler = Product.objects.filter(category__name='Tamamlayıcı Ürünler (Erkek)')

    return render(request, "etmmurun.html",{'products':etamamlayici_urunler})

def sepet(request):

    tum_urunler = Product.objects.all()


    return render (request, "sepet.html", {'sepet_urunler' :tum_urunler})

def anasayfa(request):

    return render(request, 'anasayfa.html')

def favoriler(request):

    fav_urunler = Product.objects.all()
    
    return render(request, 'favoriler.html', {'favorites':fav_urunler })

def smokin(request):

    smokin_urunler = Product.objects.filter(category__name='Smokin')

    return render(request, 'smokin.html', {'erkekurunler':smokin_urunler}) 

def kadinkategori(request):
    return render(request, 'kadın-kategori.html')

