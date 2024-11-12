# from http.client import HTTPResponse
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    Http404,
    HttpResponseRedirect,
    HttpResponsePermanentRedirect,
)
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

# menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]

data_db = [
    {
        "id": 1,
        "title": "Анджелина Джоли",
        "content": """<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.

    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».""",
        "is_published": True,
    },
    {
        "id": 2,
        "title": "Марго Робби",
        "content": "Биография Марго Робби",
        "is_published": False,
    },
    {
        "id": 3,
        "title": "Джулия Робертс",
        "content": "Биография Джулия Робертс",
        "is_published": True,
    },
]


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        "title": "Главная страница",
        "menu": menu,
        "float": 26.65,
        "posts": data_db,
    }
    return render(request, "women/index.html", context=data)


def about(request):
    return render(
        request, "women/about.html", {"title": "Страница about", "menu": menu}
    )


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Связаться с нами")


def login(request):
    return HttpResponse("Авторизоваться")


# def categories(request, cats_id):
#    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id статьи - {cats_id}</p>")


# def categories_by_slug(request, cats_slug):
#    if request.GET:
#        print(request.GET)
#   return HttpResponse(
#        f"<h1>Статьи по категориям</h1><p>Slug статьи - {cats_slug}</p>"
#    )


# def archive(request, year):
#    if year > 2023:
#        uri = reverse("cats", args=(year,))
#        return HttpResponsePermanentRedirect(uri)

#    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound(
        "<h1>Страница не найдена. Отработал page_not_found.</h1><br><a href='http://127.0.0.1:8000/'>Main</a>"
    )


# def archive(request,year):
#     if year>2050:
#         raise Http404()
#     return HttpResponse(f"<h2>Год издания - {year}</h2>")
# def page_not_found(request,exception):
#     return HttpResponseNotFound('<h1>Нет такой страницы</h1>')
