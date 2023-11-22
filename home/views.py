from django.db.models import Q
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404


#multilanguage
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response

# multilanguage code end

# Create your views here.
def homepage(request):
    books = Book.objects.all().order_by('-id')[0:5]
    news = News.objects.all().order_by('-create_date')[0:3]
    adt = Ads.objects.all().order_by('-id')[0:2]
    structure = Structure.objects.all()
    about = About.objects.all()
    history = History.objects.filter(id=1)
    history1 = History.objects.filter(id=2)
    videos = Video.objects.all()
    context = {'news': news,  'adt': adt, 'structure': structure,
                'about': about, 'books': books, 'videos': videos,
                'history': history, 'history1': history1}
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
    newspapers = Newspaper.objects.all()
    readers = Readers.objects.all()
    context = {'newspapers': newspapers, 'readers': readers}
    return render(request, 'readers.html', context) 


def catalog(request):
    b_catalog = Catalog.objects.filter(id=1)
    catalog = Catalog.objects.filter(id=2)
    el_catalog = Catalog.objects.filter(id=3)
    context = {'b_catalog': b_catalog,'catalog': catalog, 'el_catalog': el_catalog}
    return render(request, 'catalog.html', context)


def structure(request):
    structure = Structure.objects.all()
    context = {'structure': structure}
    return render(request, 'structure.html', context)


def categories(request):
    categories = Category.objects.all().order_by('id')[0:12]
    categories1 = Category.objects.all().order_by('id')[12:23]
    categories2 = Category.objects.all().order_by('id')[23:43]

    return {'categories': categories, 'categories1': categories1, 'categories2': categories2}


def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    books = Book.objects.filter(category=category)
    return render(request, 'list-category.html', {'category': category, 'books': books})


def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)


def search(request):
    search = request.GET.get('q', '').lower()

    if search:
        books = Book.objects.filter(
            Q(title__icontains=search) |
            Q(author__icontains=search) |
            Q(category__name__icontains=search)
        )
    else:
        books = Book.objects.all().order_by('-id')
    return render(request, 'books.html', {"books": books})


def photo(request):
    photos = Photo.objects.all()
    return render(request, 'photo.html', {'photos': photos})


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)

    return render(request, 'single_photo.html', {'photo': photo})



def video(request):
    return render(request, 'video.html')

def magazine(request):
    return render(request, 'magazine.html')
