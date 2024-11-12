# from multiprocessing.resource_tracker import register
# from sqlite3 import register_converter

from django.urls import path, re_path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("addpage/", views.addpage, name="add_page"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("post/<int:post_id>", views.show_post, name="post"),
    # path("cats/<int:cats_id>/", views.categories, name="cats_id"),
    # path("cats/<slug:cats_slug>/", views.categories_by_slug, name="cats"),
    # path("women/", views.index),
    # re_path(r"^archive/(?P<year>[0-9]{4})/",views.archive)
    # path("archive/<year4:year>", views.archive, name="archive"),
]
