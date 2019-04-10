from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.shortcuts import render
from .models import Character, Death

from django.http import HttpResponse


class HomeView(TemplateView):
    greeting = len(Death.objects.filter(name__gender="Female"))
    template_name = "homepage.html"

    def get(self, request):
        return render(request, self.template_name, {'greet': self.greeting})
        # return HttpResponse(self.greeting)

    def get_number(self):
        return 4
        # return len(Character.objects.select_related('death'))
    # def homepage(request):
    #     female_chars = len(Character.objects.filter(gender="Female"))
    #     male_chars = len(Character.objects.filter(gender="Male"))
    #     return render(request, 'asoiaf/homepage.html', {'female_chars': female_chars, 'male_chars': male_chars})


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

        return [[female_chars, dead_ladies], [80, male_chars]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
