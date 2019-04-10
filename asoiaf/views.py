from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class HomeView(TemplateView):
    template_name = "homepage.html"
    # def homepage(request):
    #     female_chars = len(Character.objects.filter(gender="Female"))
    #     male_chars = len(Character.objects.filter(gender="Male"))
    #     return render(request, 'asoiaf/homepage.html', {'female_chars': female_chars, 'male_chars': male_chars})


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
