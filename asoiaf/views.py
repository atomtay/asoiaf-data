from django.shortcuts import render
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView, HighchartPlotLineChartView
from chartjs.views.pie import HighChartDonutView
from django.db import connection
from .queries import MortalityByGender, LiteraryTrope


class OverviewBarChartJSON(BaseLineChartView):
    def get_labels(self):
        return ["Total", "Alive", "Dead"]

    def get_providers(self):
        return ["Male", "Female"]

    def get_data(self):
        return MortalityByGender.get_data(self)


class LiteraryTropeLineChartJSON(BaseLineChartView):
    def get_labels(self):
        return ["A Game of Thrones", "A Clash of Kings", "A Storm of Swords", "A Feast for Crows", "A Dance with Dragons"]

    def get_providers(self):
        return ["Number of chapters", "Average chapter of male death", "Average chapter of female death"]

    def get_data(self):
        return LiteraryTrope.get_data(self)


class NewLineChartJSONView(BaseLineChartView):
    def get_labels(self):
        return ["Deaths"]

    def get_providers(self):
        return ["Nobility", "Smallfolk"]

    def get_data(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(name_id) FROM asoiaf_death;")
            total_deaths = cursor.fetchall()[0]

            cursor.execute(
                "SELECT COUNT(asoiaf_death.name_id) FROM asoiaf_death INNER JOIN asoiaf_nobility ON asoiaf_death.name_id=asoiaf_nobility.name;")
            noble_deaths = cursor.fetchall()[0]

            smallfolk_deaths = total_deaths[0] - noble_deaths[0]

        return [noble_deaths, [smallfolk_deaths]]


class DeathLineJSONView(BaseLineChartView):
    # SELECT manner_of_death,count(name_id) FROM asoiaf_death WHERE manner_of_death <> 'Unknown' GROUP BY manner_of_death ORDER BY count(name_id) DESC;
    def get_labels(self):
        return ['Manner of Death']

    def get_providers(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT manner_of_death FROM asoiaf_death WHERE manner_of_death!='Unknown' GROUP BY manner_of_death ORDER BY count(name_id) DESC LIMIT 10;")
            providers = cursor.fetchall()

        return providers

    def get_data(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT count(name_id) FROM asoiaf_death WHERE manner_of_death!='Unknown' GROUP BY manner_of_death ORDER BY count(name_id) DESC LIMIT 10;")
            data = cursor.fetchall()

        return data


class DeathBookLineJSONView(BaseLineChartView):

    # SELECT asoiaf_death.manner_of_death,count(asoiaf_death.name_id),asoiaf_book_of_death.book_id FROM asoiaf_death INNER JOIN asoiaf_book_of_death ON asoiaf_death.name_id=asoiaf_book_of_death.name WHERE asoiaf_death.manner_of_death IN('Slain (sword)', 'Arrow/bolt', 'Stabbing', 'Animal', 'Beheading') GROUP BY asoiaf_book_of_death.book_id, asoiaf_death.manner_of_death ORDER BY asoiaf_book_of_death.book_id

    def get_labels(self):
        return ['Animal', 'Arrow/bolt', 'Beheading', 'Slain (sword)', 'Stabbing']

    def get_providers(self):

        return ['A Game of Thrones', 'A Clash of Kings', 'A Storm of Swords', 'A Feast for Crows', 'A Dance with Dragons']

    def get_data(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT count(asoiaf_death.name_id)book_id FROM asoiaf_death INNER JOIN asoiaf_book_of_death ON asoiaf_death.name_id=asoiaf_book_of_death.name WHERE asoiaf_death.manner_of_death IN('Slain (sword)', 'Arrow/bolt', 'Stabbing', 'Animal', 'Beheading') AND asoiaf_book_of_death.book_id=1 GROUP BY asoiaf_book_of_death.book_id, asoiaf_death.manner_of_death ORDER BY asoiaf_death.manner_of_death ASC;"
            )
            got = []
            for datapoint in cursor.fetchall():
                got.append(datapoint[0])

            cursor.execute(
                "SELECT count(asoiaf_death.name_id) FROM asoiaf_death INNER JOIN asoiaf_book_of_death ON asoiaf_death.name_id=asoiaf_book_of_death.name WHERE asoiaf_death.manner_of_death IN('Slain (sword)', 'Arrow/bolt', 'Stabbing', 'Animal', 'Beheading') AND asoiaf_book_of_death.book_id=2 GROUP BY asoiaf_book_of_death.book_id, asoiaf_death.manner_of_death ORDER BY asoiaf_death.manner_of_death ASC;"
            )
            cok = []
            for datapoint in cursor.fetchall():
                cok.append(datapoint[0])

            cursor.execute(
                "SELECT count(asoiaf_death.name_id) FROM asoiaf_death INNER JOIN asoiaf_book_of_death ON asoiaf_death.name_id=asoiaf_book_of_death.name WHERE asoiaf_death.manner_of_death IN('Slain (sword)', 'Arrow/bolt', 'Stabbing', 'Animal', 'Beheading') AND asoiaf_book_of_death.book_id=3 GROUP BY asoiaf_book_of_death.book_id, asoiaf_death.manner_of_death ORDER BY asoiaf_death.manner_of_death ASC;"
            )
            sos = []
            for datapoint in cursor.fetchall():
                sos.append(datapoint[0])

            # cursor.execute(
            #     "SELECT count(asoiaf_death.name_id) FROM asoiaf_death INNER JOIN asoiaf_book_of_death ON asoiaf_death.name_id=asoiaf_book_of_death.name WHERE asoiaf_death.manner_of_death IN('Slain (sword)', 'Arrow/bolt', 'Stabbing', 'Animal', 'Beheading') AND asoiaf_book_of_death.book_id=4 GROUP BY asoiaf_book_of_death.book_id, asoiaf_death.manner_of_death ORDER BY asoiaf_death.manner_of_death ASC;"
            # )
            # ffc = []
            # for datapoint in cursor.fetchall():
            #     ffc.append(datapoint[0])

            ffc = [1, 0, 0, 2, 2]

            cursor.execute(
                "SELECT count(asoiaf_death.name_id) FROM asoiaf_death INNER JOIN asoiaf_book_of_death ON asoiaf_death.name_id=asoiaf_book_of_death.name WHERE asoiaf_death.manner_of_death IN('Slain (sword)', 'Arrow/bolt', 'Stabbing', 'Animal', 'Beheading') AND asoiaf_book_of_death.book_id=5 GROUP BY asoiaf_book_of_death.book_id, asoiaf_death.manner_of_death ORDER BY asoiaf_death.manner_of_death ASC;"
            )
            dwd = []
            for datapoint in cursor.fetchall():
                dwd.append(datapoint[0])
        return [got, cok, sos, ffc, dwd]


home = TemplateView.as_view(template_name='home.html')
overview_bar_chart_json = OverviewBarChartJSON.as_view()
chapter_line_chart_json = LiteraryTropeLineChartJSON.as_view()
new_line_json = NewLineChartJSONView.as_view()
manner_of_death_line_chart_json = DeathLineJSONView.as_view()
death_by_book_json = DeathBookLineJSONView.as_view()
