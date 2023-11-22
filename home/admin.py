from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

# Register your models here.

class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


class CatalogAdmin(admin.ModelAdmin):
    list_display =('id','title')


class HistoryAdmin(admin.ModelAdmin):
    list_display =('id',)


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PostImageInline(admin.TabularInline):
    model = PostImage


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    inlines = [PostImageInline]

    class Meta:
        model = Photo


admin.site.register(News)
admin.site.register(Ads)
admin.site.register(About)
admin.site.register(Structure)
admin.site.register(Book, BookAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PostImage)
admin.site.register(Newspaper)
admin.site.register(Readers)
admin.site.register(Video, AdminVideo)
admin.site.register(History, HistoryAdmin)
admin.site.register(Catalog, CatalogAdmin)