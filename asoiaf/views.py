from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Book, Character, Chapter_of_Death, Book_of_Death, Death, Nobility

from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.db import connection


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        return ["Total", "Alive", "Dead"]

    def get_providers(self):
        return ["Total", "Male", "Female"]

    def get_data(self):
        chars_total = len(Character.objects.all())
        male_chars_total = len(Character.objects.filter(gender='Male'))
        female_chars_total = len(Character.objects.filter(gender='Female'))

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT name from asoiaf_character INNER JOIN asoiaf_death ON asoiaf_character.name = asoiaf_death.name_id WHERE gender = 'Male'")
            malerow = len(cursor.fetchall())

            cursor.execute(
                "SELECT name from asoiaf_character INNER JOIN asoiaf_death ON asoiaf_character.name = asoiaf_death.name_id WHERE gender = 'Female'")
            femalerow = len(cursor.fetchall())

        dead_chars_total = len(Death.objects.all())
        dead_male_chars = malerow
        dead_female_chars = femalerow

        alive_chars_total = chars_total - dead_chars_total
        alive_male_chars = male_chars_total - dead_male_chars
        alive_female_chars = female_chars_total - dead_female_chars

        return [[chars_total, alive_chars_total, dead_chars_total],
                [male_chars_total, alive_male_chars, dead_male_chars],
                [female_chars_total, alive_female_chars, dead_female_chars]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()


class NewChartJSONView(BaseLineChartView):
    def get_labels(self):
        return ["A Game of Thrones", "A Clash of Kings", "A Storm of Swords", "A Feast for Crows", "A Dance with Dragons"]

    def get_providers(self):
        return ["Male", "Female", "Total Chapter"]

    def get_data(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT num_of_chapters FROM asoiaf_book;")
            chapter_list = []
            for chapter in cursor.fetchall():
                chapter_list.append(chapter[0])

            cursor.execute("SELECT ROUND(AVG(asoiaf_chapter_of_death.chapter)) FROM asoiaf_character INNER JOIN asoiaf_chapter_of_death ON asoiaf_character.name=asoiaf_chapter_of_death.name INNER JOIN asoiaf_book_of_death ON asoiaf_character.name=asoiaf_book_of_death.name INNER JOIN asoiaf_book ON asoiaf_book.book_id=asoiaf_book_of_death.book_id WHERE asoiaf_character.\"gender\"=\'Female\' GROUP BY asoiaf_book.book_id ORDER BY asoiaf_book.book_id;")

            female_chapter_list = []
            for chapter in cursor.fetchall():
                female_chapter_list.append(chapter[0])

            cursor.execute("SELECT ROUND(AVG(asoiaf_chapter_of_death.chapter)) FROM asoiaf_character INNER JOIN asoiaf_chapter_of_death ON asoiaf_character.name=asoiaf_chapter_of_death.name INNER JOIN asoiaf_book_of_death ON asoiaf_character.name=asoiaf_book_of_death.name INNER JOIN asoiaf_book ON asoiaf_book.book_id=asoiaf_book_of_death.book_id WHERE asoiaf_character.\"gender\"=\'Male\' GROUP BY asoiaf_book.book_id ORDER BY asoiaf_book.book_id;")

            male_chapter_list = []
            for chapter in cursor.fetchall():
                male_chapter_list.append(chapter[0])
        return [male_chapter_list,
                female_chapter_list,
                chapter_list]


new_chart = TemplateView.as_view(template_name='new_chart.html')
new_chart_json = NewChartJSONView.as_view()


class DoughnutJSONView(BaseLineChartView):
    def get_labels(self):
        # return ['Read', 'Write', 'Yes', 'No']
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT asoiaf_death.manner_of_death, COUNT(asoiaf_character.gender) FROM asoiaf_death INNER JOIN asoiaf_character ON asoiaf_death.name_id=asoiaf_character.name WHERE asoiaf_death.\"manner_of_death\" <> 'Unknown' AND asoiaf_character.\"gender\"='Male' GROUP BY asoiaf_death.manner_of_death ORDER BY asoiaf_death.manner_of_death ASC;")
            male_death_types = []
            for type in cursor.fetchall():
                male_death_types.append(male_death_types[0])
            return male_death_types

    def get_providers(self):
        return ["Manner of Death"]

    def get_data(self):
        return [4, 6, 3, 6]
        # All manners and total count
        # SELECT asoiaf_death.manner_of_death,COUNT(asoiaf_character.gender) FROM asoiaf_death INNER JOIN asoiaf_character ON asoiaf_death.name_id=asoiaf_character.name WHERE asoiaf_death."manner_of_death" <> 'Unknown' GROUP BY asoiaf_death.manner_of_death ORDER BY asoiaf_death.manner_of_death ASC;

        # Male death counts
        # SELECT asoiaf_death.manner_of_death,COUNT(asoiaf_character.gender) FROM asoiaf_death INNER JOIN asoiaf_character ON asoiaf_death.name_id=asoiaf_character.name WHERE asoiaf_death."manner_of_death" <> 'Unknown' AND asoiaf_character."gender"='Male' GROUP BY asoiaf_death.manner_of_death ORDER BY asoiaf_death.manner_of_death ASC;

        # Male death categories
        # SELECT asoiaf_death.manner_of_death FROM asoiaf_death INNER JOIN asoiaf_character ON asoiaf_death.name_id=asoiaf_character.name WHERE asoiaf_death."manner_of_death" <> 'Unknown' AND asoiaf_character."gender"='Male' GROUP BY asoiaf_death.manner_of_death ORDER BY asoiaf_death.manner_of_death ASC;

        # Female death counts
        # SELECT asoiaf_death.manner_of_death,COUNT(asoiaf_character.gender) FROM asoiaf_death INNER JOIN asoiaf_character ON asoiaf_death.name_id=asoiaf_character.name WHERE asoiaf_death."manner_of_death" <> 'Unknown' AND asoiaf_character."gender"='Female' GROUP BY asoiaf_death.manner_of_death ORDER BY asoiaf_death.manner_of_death ASC;

        # Female death categories
        # SELECT asoiaf_death.manner_of_death FROM asoiaf_death INNER JOIN asoiaf_character ON asoiaf_death.name_id=asoiaf_character.name WHERE asoiaf_death."manner_of_death" <> 'Unknown' AND asoiaf_character."gender"='Female' GROUP BY asoiaf_death.manner_of_death ORDER BY asoiaf_death.manner_of_death ASC;


doughnut = TemplateView.as_view(template_name='doughnut_chart.html')
doughnut_json = DoughnutJSONView.as_view()
