from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Book
import requests
from django.http import HttpResponse


# class HomeView(TemplateView):
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
    # return HttpResponse('<pre>' + requests.get('http://httpbin.org/status/418').text + '</pre>')
    # def get(self, request):
    #     sample_book = Book.objects.filter(title="A Game of Thrones")
    #     return render(request, "homepage.html")


# class LineChartJSONView(BaseLineChartView):
#     def get_labels(self):
#         return ["Alive", "Dead"]

#     def get_providers(self):
#         """Return names of datasets."""
#         return ["Female", "Male"]

#     def get_data(self):
#         """Return 3 datasets to plot."""
#         female_chars = len(Character.objects.filter(gender="Female"))
#         male_chars = len(Character.objects.filter(gender="Male"))

#         dead_ladies = len(Character.objects.select_related('death'))

#         return [[female_chars, dead_ladies], [80, male_chars]]


# line_chart = TemplateView.as_view(template_name='line_chart.html')
# line_chart_json = LineChartJSONView.as_view()
