#from http.client import HTTPResponse
from django.http import HttpResponse,HttpResponseNotFound,Http404

from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Страница индекс1234")

def categories(request,cats_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id статьи - {cats_id}</p>")

def categories_by_slug(request,cats_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Slug статьи - {cats_slug}</p>")

def archive(request,year):
    if year>2050:
        raise Http404()
    return HttpResponse(f"<h2>Год издания - {year}</h2>")
def page_not_found(request,exception):
    return HttpResponseNotFound('<h1>Нет такой страницы</h1>')
