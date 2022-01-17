from django.db import models

# Create your models here.
# https://djbook.ru/rel3.0/ref/models/index.html
# при создании или изменении класса выполняем следующие команды:
#   python manage.py makemigrations
#   python manage.py migrate


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

# метод вывода информации объекта
    def __str__(self):
        return self.title

# from women.models import Women команда для shell
# from django.db import connection
# https://djbook.ru/rel3.0/topics/db/