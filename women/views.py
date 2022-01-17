from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

# Create your views here.
menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts,'menu':menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'menu':menu, 'title': 'О сайте'})

def categories(request, cat_id):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статья по категориям</h1><p>{cat_id}</p>")

def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)  # перенаправление
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


# функция обработки страницы 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

