from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),


]
