from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Book, Character, Chapter_of_Death, Book_of_Death, Death, Nobility

from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

from django.http import HttpResponse


class HomeView(TemplateView):

    book = Character.objects.filter(name="Lysa Tully")[0].name

    def get(self, request):
        return render(request, "homepage.html", {'book': self.book})

    #     female_chars = len(Character.objects.filter(gender="Female"))
    #     male_chars = len(Character.objects.filter(gender="Male"))


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        return ["Alive", "Dead"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Female", "Male"]

    def get_data(self):
        """Return 3 datasets to plot."""

        female_chars = len(Character.objects.filter(gender="Female"))
        male_chars = len(Character.objects.filter(gender="Male"))
        dead_ladies = len(Character.objects.select_related('death'))
        return [[60, female_chars], [male_chars, dead_ladies]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
