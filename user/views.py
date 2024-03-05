from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def userRegister(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form' : form
    }

    return render(request, 'register.html', context)