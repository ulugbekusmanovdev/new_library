from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('news/', views.news, name='news'),
    path('adt/', views.adt, name='adt'),
    path('readers/', views.readers, name='readers'),
    path('catalog/', views.catalog, name='catalog'),
    path('structure/', views.structure, name='structure'),
    path('books/', views.books, name='books'),
    path('search', views.search, name='search'),
    path('photo/', views.photo, name='photo'),
    path('video/', views.video, name='video'),
    path('magazine/', views.magazine, name='magazine'),
    path('photo_detail/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),

    path("<str:language>", views.set_language, name="set-language"),
]