from django.shortcuts import render, redirect
from .models import *
from urunler.models import CartItem
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    return render(request, "kozmetik.html", {'kozmetiks': kozmetik_urunler})

def tamamlayici(request):

    tamamlayici_urunler = Product.objects.filter(category__name='Tamamlayıcı Ürünler (Kadın)')

    return render(request, "ktmmurun.html", {'kozmetiks': tamamlayici_urunler})

def taki(request):
    taki_urunler = Product.objects.filter(category__name='Takı')
    return render(request, "taki.html", {'kozmetiks': taki_urunler})

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

    return render(request, "etmmurun.html",{'kozmetiks':etamamlayici_urunler})

def sepet(request):
    sepet_urunler = CartItem.objects.filter(cart__user=request.user)

    return render(request, "sepet.html", {'sepet_urunler': sepet_urunler})

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




def add_to_cart(request):
    if request.method == 'POST':
        urun_adi = request.POST['urun_adi']
        urun_fiyati = request.POST['urun_fiyati']
        urun_resmi = request.POST['urun_resmi']
        beden = request.POST['beden']

        # Ürünü alın veya yeni birini oluşturun
        product, created = Product.objects.get_or_create(
            name=urun_adi,
            defaults={'price': urun_fiyati, 'image_url': urun_resmi}
        )

        # Yeni bir Cart oluşturun veya mevcut birini alın
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Mevcut bir CartItem varsa miktarını güncelleyin, yoksa yeni birini oluşturun
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            size=beden,
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('sepet')

    return redirect('index')


    
def sepet(request):
    sepet_urunler = CartItem.objects.filter(cart__user=request.user)

    return render(request, "sepet.html", {'sepet_urunler': sepet_urunler})

def sepet_sil(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('sepet')

def hakkimizda(request):
    return render(request, 'hakkimizda.html')

def iletisim(request):
    return render(request, "iletisim.html")

def send_message(request):
    if request.method == 'POST':
        # Formdan gelen verileri al
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Burada mesajı işleyebilirsiniz, örneğin bir e-posta gönderebilirsiniz
        
        # İletişim formunun gönderildiği sayfaya yeniden yönlendirme
        return HttpResponseRedirect(reverse('iletisim'))
    else:
        # POST dışındaki herhangi bir istekte sayfaya geri dönme
        return HttpResponseRedirect(reverse('iletisim'))