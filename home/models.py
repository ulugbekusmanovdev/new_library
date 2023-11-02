from django.db import models
from django.urls import reverse


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинки')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    news_view = models.IntegerField(default=0)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.title} - {self.create_date}'


class Ads(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Обявление'
        verbose_name_plural = 'Обявление'

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    info = models.TextField()
    history = models.TextField()

    def __str__(self):
        return self.title


class Structure(models.Model):
    director = models.CharField(max_length=200, null=True, blank=True)
    director_info = models.TextField()
    d_img = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default.png',
                              verbose_name='Картинки')
    ibo = models.CharField(max_length=200, null=True, blank=True)
    ibo_info = models.TextField()
    ibo_img = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default.png',
                                verbose_name='Картинки')
    e_res = models.CharField(max_length=200, blank=True)
    e_res_info = models.TextField(blank=True)
    e_res_img = models.ImageField(upload_to='avatars/', blank=True, default='avatars/default.png',
                                  verbose_name='Картинки')

    def __str__(self):
        return f'{self.director} - {self.ibo}'


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Категория'
        ordering = ('-id',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.SlugField(max_length=100, verbose_name='слаг')
    author = models.CharField(max_length=100, verbose_name='автор')
    year = models.CharField(max_length=100, verbose_name='год')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    pdf = models.FileField(upload_to='book/pdfs/')
    photo = models.ImageField(upload_to='book/photos/', null=True, blank=True)
    recommended_books = models.BooleanField(default=False, verbose_name='рекомендовано')
    top_books = models.BooleanField(default=False, verbose_name='топ')
    business_books = models.BooleanField(default=False, verbose_name='бизнес')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книги"
        verbose_name_plural = "Книги"
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('books', args=[self.slug])


class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    photo_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Картинки'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Photo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/')


class Newspaper(models.Model):
    number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Газета'
        verbose_name_plural = 'Газета'
        ordering = ('id',)
