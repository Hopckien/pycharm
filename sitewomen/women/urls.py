from multiprocessing.resource_tracker import register
#from sqlite3 import register_converter

from django.urls import path,re_path,register_converter
from . import views,converters

register_converter(converters.FourDigitYearConverter,"year4")

urlpatterns = [
    path('women/', views.index),
    path('cats/<int:cats_id>/', views.categories),
    path('cats/<slug:cats_slug>/', views.categories_by_slug),
    path('', views.index),
    #re_path(r"^archive/(?P<year>[0-9]{4})/",views.archive)
    path('archive/<year4:year>',views.archive)

]