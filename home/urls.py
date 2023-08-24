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
]