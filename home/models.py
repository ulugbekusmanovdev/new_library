from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинки')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    news_view = models.IntegerField(default=0)

    class Meta:
        ordering = ('-create_date',)
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.title} - {self.create_date}'
    

class Ads(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата')

    class Meta:
        ordering = ('-create_date',)
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
    d_img = models.ImageField(upload_to='avatars/',null=True, blank=True, default='avatars/default.png', verbose_name='Картинки')
    ibo = models.CharField(max_length=200, null=True, blank=True)
    ibo_info = models.TextField()
    ibo_img = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default.png', verbose_name='Картинки')
    e_res = models.CharField(max_length=200, blank=True)
    e_res_info = models.TextField(blank=True)
    e_res_img = models.ImageField(upload_to='avatars/', blank=True, default='avatars/default.png', verbose_name='Картинки')

    def __str__(self):
        return f'{self.director} - {self.ibo}'