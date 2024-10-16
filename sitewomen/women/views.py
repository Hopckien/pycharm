#from http.client import HTTPResponse
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = ["О сайте","Добавить статью","Обратная связь","Войти"]


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float':26.65,
    }
    return render(request, 'women/index.html',context=data)

def about(request):
    return render(request, 'women/about.html', {'title': 'Страница about'})

def categories(request,cats_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id статьи - {cats_id}</p>")

def categories_by_slug(request,cats_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Slug статьи - {cats_slug}</p>")

def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('sport', ))
        return HttpResponsePermanentRedirect(uri)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

# def archive(request,year):
#     if year>2050:
#         raise Http404()
#     return HttpResponse(f"<h2>Год издания - {year}</h2>")
# def page_not_found(request,exception):
#     return HttpResponseNotFound('<h1>Нет такой страницы</h1>')

