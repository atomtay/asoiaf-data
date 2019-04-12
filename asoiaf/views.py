from django.shortcuts import render
from .models import Book, Character, Chapter_of_Death, Book_of_Death, Death, Nobility
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView, HighchartPlotLineChartView
from chartjs.views.pie import HighChartDonutView
from django.db import connection

home = TemplateView.as_view(template_name='home.html')


class BarChartJSONView(BaseLineChartView):

    def get_labels(self):
        return ["Total", "Alive", "Dead"]

    def get_providers(self):
        return ["Male", "Female"]

    def get_data(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT count(name) from asoiaf_character WHERE \"gender\"='Male';"
            )
            total_males = cursor.fetchone()

            cursor.execute(
                "SELECT count(name) from asoiaf_character WHERE \"gender\"='Female';"
            )
            total_females = cursor.fetchone()
            cursor.execute(
                "SELECT count(name) from asoiaf_character INNER JOIN asoiaf_death ON asoiaf_character.name=asoiaf_death.name_id WHERE asoiaf_character.\"gender\" = 'Male';")
            male_deaths = cursor.fetchone()

            cursor.execute("SELECT count(name) from asoiaf_character INNER JOIN asoiaf_death ON asoiaf_character.name=asoiaf_death.name_id WHERE asoiaf_character.\"gender\"=\'Female\';"
                           )

            female_deaths = cursor.fetchone()

            alive_males = total_males[0]-male_deaths[0]
            alive_females = total_females[0]-female_deaths[0]

        return [[total_males[0], alive_males, male_deaths[0]], [total_females[0], alive_females, female_deaths[0]]]

        # dead_male_chars = malerow
        # dead_female_chars = femalerow

        # alive_male_chars = male_chars_total - dead_male_chars
        # alive_female_chars = female_chars_total - dead_female_chars

        # return [[male_chars_total, alive_male_chars, dead_male_chars],
        #         [female_chars_total, alive_female_chars, dead_female_chars]]


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        return ["A Game of Thrones", "A Clash of Kings", "A Storm of Swords", "A Feast for Crows", "A Dance with Dragons"]

    def get_providers(self):
        return ["Number of chapters", "Average chapter of male death", "Average chapter of female death"]

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
        return [chapter_list,
                male_chapter_list,
                female_chapter_list]


class NewLineChartJSONView(BaseLineChartView):
    def get_labels(self):
        return ["Deaths"]

    def get_providers(self):
        return ["Nobility", "Commonfolk"]

    def get_data(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(name_id) FROM asoiaf_death;")
            total_deaths = cursor.fetchall()[0]

            cursor.execute(
                "SELECT COUNT(asoiaf_death.name_id) FROM asoiaf_death INNER JOIN asoiaf_nobility ON asoiaf_death.name_id=asoiaf_nobility.name;")
            noble_deaths = cursor.fetchall()[0]

            commonfolk_deaths = total_deaths[0] - noble_deaths[0]

        return [noble_deaths, [commonfolk_deaths]]


overview_bar_chart_json = BarChartJSONView.as_view()
chapter_line_chart_json = LineChartJSONView.as_view()
new_line_json = NewLineChartJSONView.as_view()
