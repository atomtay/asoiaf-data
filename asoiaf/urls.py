from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url

from . import views

urlpatterns = [

    path('line_chart', views.line_chart),
    url(r'^line_chart/json/$', views.line_chart_json,
        name='line_chart_json'),
    url(r'^new_chart/$', views.new_chart,
        name='new_chart'),
    url(r'^new_chart/json/$', views.new_chart_json,
        name='new_chart_json'),

]
