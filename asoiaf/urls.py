from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url

from . import views

urlpatterns = [

    path('', views.home, name="home"),
    url(r'^overview_bar_chart/json/$', views.overview_bar_chart_json,
        name='overview_bar_chart_json'),
    url(r'^chapter_line_chart/json/$', views.chapter_line_chart_json,
        name='chapter_line_chart_json'),
    url(r'^new_chart/json/$', views.new_line_json,
        name='new_line_json'),
    url(r'^manner_of_death_chart/json/$', views.manner_of_death_line_chart_json,
        name='manner_of_death_line_chart_json'),

]
