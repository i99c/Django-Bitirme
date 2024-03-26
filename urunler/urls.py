from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', index, name='index'),
    path('abiye/', abiye, name='abiye'),
    path('kadin-ayakkabi/', kadinAyakkabi, name='kayakkabi'),
    path('kozmetik/', kozmetik, name='kozmetik'),
    path('tamamlayici/', tamamlayici, name='ktmmurun'),
    path('taki/', taki, name='taki'),
    path('gomlek/', gomlek, name='gomlek'),
    path('takim/', takim, name='takim'),
    path('ceket/', ceket, name='ceket'),
    path('yelek/', yelek, name='yelek'),
    path('erkek-ayakkabi/', eayakkabi, name='eayakkabi'),
    path('erkek-tamamlayici/', etmmurun, name='etmmurun'),
    path('sepet/', sepet, name='sepet'),
    path('anasayfa/', anasayfa, name='anasayfa'),
    path('favoriler/', favoriler, name='favoriler'),
    path('smokin/',smokin,name='smokin'),
    path('hakkimizda/', hakkimizda, name='hakkimizda'),
    path('iletisim/', iletisim, name='iletisim'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('sepet/', views.sepet, name='sepet'),
    path('sepet/<int:cart_item_id>/sil/', views.sepet_sil, name='sepet_sil'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('send_message/', views.send_message, name='send_message'),
]

