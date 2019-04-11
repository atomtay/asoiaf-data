from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Book, Character, Chapter_of_Death, Book_of_Death, Death, Nobility

from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.db import connection


class HomeView(TemplateView):
    def my_custom_sql(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT name from asoiaf_character INNER JOIN asoiaf_death ON asoiaf_character.name = asoiaf_death.name_id WHERE gender = 'Male'")
            row = len(cursor.fetchall())

        return row

    dead = Death.objects.all()
    male = Character.objects.filter(gender='Male')
    # dead_male_chars = len  Character.objects.select_related('asoiaf_nobility.name'))

    #len(Character.objects.filter(   death__name='Robert Baratheon'))

    def get(self, request):
        return render(request, "homepage.html", {'book': self.my_custom_sql})


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        return ["Total", "Alive", "Dead"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Total", "Male", "Female"]

    def my_custom_sql(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT name from asoiaf_character INNER JOIN asoiaf_death ON asoiaf_character.name = asoiaf_death.name_id WHERE gender = 'Male'")
            row = len(cursor.fetchall())

        return row

    def get_data(self):
        """Return 3 datasets to plot."""

        chars_total = len(Character.objects.all())
        male_chars_total = len(Character.objects.filter(gender='Male'))
        female_chars_total = len(Character.objects.filter(gender='Female'))

        dead_chars_total = len(Death.objects.all())

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT name from asoiaf_character INNER JOIN asoiaf_death ON asoiaf_character.name = asoiaf_death.name_id WHERE gender = 'Male'")
            malerow = len(cursor.fetchall())

            cursor.execute(
                "SELECT name from asoiaf_character INNER JOIN asoiaf_death ON asoiaf_character.name = asoiaf_death.name_id WHERE gender = 'Female'")
            femalerow = len(cursor.fetchall())
        dead_male_chars = malerow
        dead_female_chars = femalerow

        # SELECT count(name) from asoiaf_character INNER JOIN asoiaf_death ON asoiaf_character.name = asoiaf_death.name_id WHERE "gender" = 'Male'

        # dead_male_chars = 0
        # dead_male_chars = len(Death.objects.filter(character__gender='Male'))
        # dead_male_chars = len(Death.objects.select_related('name'))

        # Person.objects.raw(
        #     'SELECT count(name) from asoiaf_character INNER JOIN asoiaf_death ON asoiaf_character.name=asoiaf_death.name_id WHERE "gender"=\'Male\'')

        alive_chars_total = chars_total - dead_chars_total
        alive_male_chars = male_chars_total - dead_male_chars
        alive_female_chars = female_chars_total - dead_female_chars

        # all characters
        return [[chars_total, alive_chars_total, dead_chars_total],
                [male_chars_total, alive_male_chars, dead_male_chars],
                [female_chars_total, alive_female_chars, dead_female_chars]]
        # male characters only
        # [len(male_chars_total), len(alive_male_chars), 0],
        # [len(female_chars_total), len(alive_female_chars), len(dead_female_chars)]]  # female characters only


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
