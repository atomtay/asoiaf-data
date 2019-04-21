from django.db import connection


def get_data(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(character_id) FROM death_manner;")
        total_deaths = cursor.fetchall()[0]

        cursor.execute(
            "SELECT COUNT(death_manner.character_id) FROM death_manner INNER JOIN nobility ON death_manner.character_id=nobility.character_id;")
        noble_deaths = cursor.fetchall()[0]

        smallfolk_deaths = total_deaths[0] - noble_deaths[0]

    return [noble_deaths, [smallfolk_deaths]]
