from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', HomeView.as_view()),
    path('line_chart/', views.line_chart,
         name='line_chart'),
    url(r'^line_chart/json/$', views.line_chart_json,
        name='line_chart_json'),

]
