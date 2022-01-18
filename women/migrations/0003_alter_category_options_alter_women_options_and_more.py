# Generated by Django 4.0.1 on 2022-01-18 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_category_women_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['time_create', 'title'], 'verbose_name': 'Известные женщины', 'verbose_name_plural': 'Известные женщины'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='women',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='women.category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='women',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='women',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='women',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='women',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='время редактирования'),
        ),
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
