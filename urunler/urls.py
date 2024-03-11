from django.urls import path
from .views import *

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
   
]
