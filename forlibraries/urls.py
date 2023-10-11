from django.urls import path
from . import views

urlpatterns = [
    path('personal/', views.personal, name='personal'),
    path('login/', views.login, name='login'),
]