from django.contrib import admin
from .models import News, Ads, About, Structure, Category, Book, Photo, PostImage, Newspaper
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


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