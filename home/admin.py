from django.contrib import admin
from .models import News, Ads, About, Structure
# Register your models here.

admin.site.register(News)
admin.site.register(Ads)
admin.site.register(About)
admin.site.register(Structure)