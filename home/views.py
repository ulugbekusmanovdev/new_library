from django.shortcuts import render
from .models import News, Ads, About, Structure
from django.shortcuts import get_object_or_404

# Create your views here.
def homepage(request):
    news = News.objects.all().order_by('-create_date')[0:3]
    about = About.objects.all()
    adt = Ads.objects.all()
    structure = Structure.objects.all()
    about = About.objects.all()
    context = {'news': news, 'about': about, 'adt': adt, 'structure': structure, 'about': about}
    return render(request, 'home.html', context)

def news(request):
    news = News.objects.all()

    contex = {'news': news}
    return render(request, 'news.html', contex)

def adt(request):
    adt = Ads.objects.all()
    contex = {'adt': adt}
    return render(request, 'adt.html', contex)

def readers(request):
    return render(request, 'readers.html')

def catalog(request):
    return render(request, 'catalog.html')

def structure(request):
    structure = Structure.objects.all()
    contex = {'structure': structure}
    return render(request, 'structure.html', contex)

def books(request):
    return render(request, 'books.html')

