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
    url(r'^deaths_doughnut_graph/json/$', views.deaths_doughnut_graph_json,
        name='deaths_doughnut_graph_json')

]
