from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"index.html")

def abiye(request):
    return render(request,"abiye.html")

def kadinAyakkabi(request):
    return render(request, "kayakkabi.html")

def kozmetik(request):
    return render(request, "kozmetik.html")

def tamamlayici(request):
    return render(request, "ktmmurun.html")

def taki(request):
    return render(request, "taki.html")

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