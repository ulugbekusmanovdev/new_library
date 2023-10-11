from django.shortcuts import render
from .models import *

# Create your views here.

# def slider(request):
# 	product = Product.objects.first()
# 	context = {'product':product}
# 	return render(request, 'slider.html', context)

def personal(request):
    return render(request, 'personal.html')

def login(request):
    return render(request, 'login.html')