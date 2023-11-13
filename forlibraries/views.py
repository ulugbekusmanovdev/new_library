from django.shortcuts import render
from .models import *

# Create your views here.

# def slider(request):
# 	product = Product.objects.first()
# 	context = {'product':product}
# 	return render(request, 'slider.html', context)

def personal(request):
    irbis = Irbis.objects.all()
    return render(request, 'personal.html', {'irbis': irbis})

def login(request):
    return render(request, 'login.html')

def video(request):
    return render(request, 'videos1.html')