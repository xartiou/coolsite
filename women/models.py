from django.db import models

# Create your models here.
# https://djbook.ru/rel3.0/ref/models/index.html
# при создании или изменении класса выполняем следующие команды:
#   python manage.py makemigrations
#   python manage.py migrate
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

# метод вывода информации объекта
    def __str__(self):
        return self.title

# метод для формирования url
    def get_absolute_url(self):
        return reverse ('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    # метод для формирования url
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


# from women.models import Women команда для shell
# from django.db import connection
# https://djbook.ru/rel3.0/topics/db/