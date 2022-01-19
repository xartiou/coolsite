from django.db import models

# Create your models here.
# https://djbook.ru/rel3.0/ref/models/index.html
# при создании или изменении класса выполняем следующие команды:
#   python manage.py makemigrations
#   python manage.py migrate
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="время редактирования")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    # вложенный класс для настройки модели
    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create', 'title']

    # метод вывода информации объекта
    def __str__(self):
        return self.title

    # метод для формирования url
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['id']

    def __str__(self):
        return self.name

    # метод для формирования url
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

# from women.models import Women команда для shell
# from django.db import connection
# https://djbook.ru/rel3.0/topics/db/
